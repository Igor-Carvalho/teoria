"""Módulo que contém as tarefas locais utilizadas com invoke."""

import invoke


@invoke.task
def collectstatic(ctx, settings='development', noinput=True, clear=False):
    """Coleta arquivos estáticos."""
    ctx.run('yarn install', echo=True, pty=True)
    noinput = '--noinput' if noinput else ''
    clear = '--clear' if clear else ''
    cmd = './manage.py collectstatic {} {} --settings=teoria.settings.{}'
    cmd = cmd.format(noinput, clear, settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def assetsbuild(ctx, settings='development', noinput=True, clear=True):
    """Constroe bundles."""
    collectstatic(ctx, settings, noinput, clear)
    cmd = './manage.py assets build'
    ctx.run(cmd, echo=True, pty=True)


@invoke.task(default=True)
def run_server(ctx, settings='development', noinput=True, clear=False):
    """Executa o servidor web."""
    assetsbuild(ctx, settings, noinput, clear)
    cmd = './manage.py runserver 0.0.0.0:8000 --settings=teoria.settings.{}'.format(settings)
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def distribuir(ctx, settings='production', noinput=True, clear=True):
    """Comando utilizado no git hook post-merge para efetuar as configurações do projeto em produção."""
    ctx.run('pipenv install')
    ctx.run('./manage.py migrate')
    assetsbuild(ctx, settings, noinput, clear)
    ctx.run('sudo service nginx restart')
    ctx.run('sudo service gunicorn restart')


@invoke.task
def test(ctx, tests='', settings='test'):
    """Testa as aplicações do projeto (com exceção dos testes funcionais)."""
    cmd = 'coverage run ./manage.py test {} --settings=teoria.settings.{}'.format(tests, settings)
    ctx.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    ctx.run(cmd, echo=True, pty=True)


@invoke.task
def functional_tests(ctx, package='functional_tests.histories', settings='test'):
    """Executa os testes funcionais."""
    collectstatic(ctx, settings, True)
    cmd = 'coverage run ./manage.py test {} . --settings=teoria.settings.{}'
    cmd = cmd.format(package, settings)
    ctx.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    ctx.run(cmd, echo=True, pty=True)
