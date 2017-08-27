"""Testes de visões da aplicação inscritos."""

from django.core import mail, urlresolvers
from post_office.models import EmailTemplate
from rest_framework import status, test

from .. import models


class InscritoViewSetTests(test.APITestCase):
    """Checa o conjunto de visões para inscritos."""

    @classmethod
    def setUpTestData(cls):
        """Dependências dos testes."""
        super(InscritoViewSetTests, cls).setUpTestData()
        cls.inscritos_url = urlresolvers.reverse('v1:inscrito-list')
        cls.inscritos_ativar_url = urlresolvers.reverse('v1:inscrito-ativar')

        EmailTemplate.objects.create(
            name='ativação_de_inscrito',
            subject='Ativação de inscrição',
            content='Olá, {{ inscrito.email }}!',
            html_content='<p>Olá, {{ inscrito.email }}!</p>'
        )

    def test_criação_de_inscrito(self):
        """Verifica se um inscrito é criado com um hash único e um email de confirmação é enviado."""
        # inicialmente não há mensagens de email e nenhum inscrito cadastrado.
        self.assertEqual(len(mail.outbox), 0)
        self.assertEqual(models.Inscrito.objects.count(), 0)

        # um leitor se inscreve no blog.
        data = {'email': 'test@test.org'}
        response = self.client.post(self.inscritos_url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))

        # um inscrito é criado mas não ativo.
        self.assertEqual(models.Inscrito.objects.count(), 1)
        inscrito = models.Inscrito.objects.get(pk=response.data['id'])
        self.assertEqual(inscrito.email, data['email'])
        self.assertFalse(inscrito.ativo)

        chave_inicial_inscrito = inscrito.chave
        self.assertEqual(len(chave_inicial_inscrito), 64)

        # um email é enviado.
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertTrue('Olá, test@test.org' in email.body)

        # caso um email já cadastrado seja submetido novamente, não ocorre a criação de um novo inscrito, mas
        # nesse caso um outro email de confirmação é enviado.
        response = self.client.post(self.inscritos_url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))

        self.assertEqual(models.Inscrito.objects.count(), 1)
        inscrito = models.Inscrito.objects.get(pk=response.data['id'])
        self.assertEqual(inscrito.email, data['email'])
        self.assertFalse(inscrito.ativo)

        self.assertEqual(len(chave_inicial_inscrito), 64)
        self.assertEqual(len(mail.outbox), 2)
        email = mail.outbox[-1]
        self.assertTrue('Olá, test@test.org' in email.body)

    def test_ativação_de_inscrito(self):
        """Verifica se o usuário é ativado corretamente."""
        self.assertEqual(len(mail.outbox), 0)

        data = {'email': 'test@test.org'}
        response = self.client.post(self.inscritos_url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(mail.outbox), 1)

        inscrito = models.Inscrito.objects.get(pk=response.data['id'])

        response = self.client.get(self.inscritos_ativar_url, {'chave': inscrito.chave})
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['mensagem'], 'Inscrito ativado com sucesso.')

        inscrito.refresh_from_db()
        self.assertIsNone(inscrito.chave)
        self.assertTrue(inscrito.ativo)

        # ao tentar inscrever um usuário ativo, nenhum email é enviado.
        response = self.client.post(self.inscritos_url, data, format='json')
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(mail.outbox), 1)
        self.assertTrue(response.data['ativo'])

        # tentar inscrever sem chave, ou com chave uma inválida não é permitido
        response = self.client.get(self.inscritos_ativar_url, {'chave': inscrito.chave})
        self.assertEqual(response.status_code, 404)

        response = self.client.get(self.inscritos_ativar_url, {})
        self.assertEqual(response.status_code, 404)

        response = self.client.get(self.inscritos_ativar_url, {'chave': ''})
        self.assertEqual(response.status_code, 404)
