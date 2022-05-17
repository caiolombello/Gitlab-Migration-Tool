# Migração Gitlab

Uma ferramenta de migração automatizada usando [Gitlab API](https://docs.gitlab.com/ee/api/).

## Funcionalidades

### Estrutura

- [ ] Transferência de grupos
- [ ] Transferência de subgrupos
- [x] Transferência de projetos*
- [x] Exclusão de projetos
- [ ] Mantém a mesma organização estrutural do ambiente

### Conteúdo

- [x] Migração do conteúdo dos repositórios*
- [x] Migração das variáveis de ambiente para seus devidos projetos*
- [ ] Migração dos Runners* (nenhuma possibilidade encontrada)

### Usuários

- [x] Transferência de usuários*
  - [x] Nome
  - [x] Usuário
  - [x] Email (usuario@vertigo.com.br)

\* Salva seus respectivos arquivos em seus diretórios propriamente criados.

## Requisitos

### Client-side

- Máquina registrada com chave SSH em ambos ambientes no Gitlab
- Chave RSA
- Token de acesso de ambos ambientes no Gitlab
- Função de usuário do Gitlab como Dono
- Espaço para armazenamento de arquivos dos repositórios
- Python >= 3.8
  - colorama
  - requests
  - urllib3
  - chardet
- Git

### Server-side

- SSH configurado devidamente com a porta 22 aberta

## Rodando em Docker

1. Variáveis precisam ser definidas:

```bash
export RSA=(RSA path)
export OLD_ORIGIN_API=(example: https://gitlab.com/api/v4/)
export OLD_ORIGIN_TOKEN=(old origin access token)
export ORIGIN_API=(example: http://localhost:8080/api/v4/projects)
export ORIGIN_TOKEN=(origin access token)
```

2. Rodando o Docker:

```bash
docker build \
--build-arg RSA=RSA \
--build-arg OLD_ORIGIN_API=OLD_ORIGIN_API \
--build-arg OLD_ORIGIN_TOKEN=OLD_ORIGIN_TOKEN \
--build-arg ORIGIN_API=ORIGIN_API \
--build-arg ORIGIN_TOKEN=ORIGIN_TOKEN \
-t gitlab-export .
```

## Utilização

1. Gere um token em: <https://gitlab.com/-/profile/personal_access_tokens>
2. Exporte o token: `export OLD_ORIGIN_TOKEN=(token gerado)`
3. Gere uma chave RSA: `ssh-keygen`
4. Exporte o caminho para chave pública: `export RSA=~/.ssh/id_rsa.pub`
5. Registre sua máquina com o RSA em: <https://gitlab.com/-/profile/keys>
6. Desabilite StrictHostKeyChecking na configuração do SSH:`echo 'StrictHostKeyChecking' > ~/.ssh/config`
7. Gere outro token em: <https://localhost:8080/-/profile/personal_access_tokens>
8. Exporte o token: `export ORIGIN_TOKEN=(token gerado)`
9. Registre sua máquina com o RSA em: <http://localhost:8080/-/profile/keys>
10. Defina as variáveis:

```bash
export OLD_ORIGIN_API=(example: https://gitlab.com/api/v4/)
export ORIGIN_API=(example: http://localhost:8080/api/v4/)
```

11. Baixe o repositório:

```bash
git clone git@gitlab.com:vertigobr/devops/rea-de-testes/caio-barbieri/exportacao-gitlab.git && cd exportacao-gitlab
```

12. Rode:

```bash
python3 get-all.py && \
python3 post-all.py && \
python3 transfer-users
```