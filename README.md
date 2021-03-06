# Migração Gitlab

Uma ferramenta de migração automatizada usando [Gitlab API](https://docs.gitlab.com/ee/api/).

## Funcionalidades

### Estrutura

- [x] Transferência de grupos*
- [x] Transferência de subgrupos*
- [x] Transferência de projetos*
- [x] Exclusão de projetos
- [x] Mantém a mesma organização estrutural do ambiente

### Conteúdo

- [x] Migração do conteúdo dos repositórios*
- [x] Migração das variáveis de ambiente para seus devidos projetos*

### Usuários

- [x] Transferência de usuários*
  - [x] Nome
  - [x] Usuário
  - [x] Email (usuario@vertigo.com.br)

\* Salva seus respectivos arquivos em seus diretórios propriamente criados.

## Requisitos

### Client-side

- Token de acesso de ambos ambientes no Gitlab
- Função de usuário do Gitlab como Dono
- Espaço para armazenamento de arquivos dos repositórios
- Git
- Python >= 3.8
  - colorama
  - requests
  - urllib3
  - chardet

## Rodando em Docker

1. [Exporte e Importe seus Grupos](https://docs.gitlab.com/ee/user/group/settings/import_export.html)

2. Variáveis precisam ser definidas:

```bash
export SOURCE_ID=# id do grupo raiz do ambiente antigo
export OLD_ORIGIN_USER=# usuário do ambiente antigo
export OLD_ORIGIN_API=# api do ambiente antigo. exemplo: https://gitlab.com/api/v4/
export OLD_ORIGIN_TOKEN= # token de acesso do ambiente antigo (https://gitlab.com/-/profile/personal_access_tokens)
export ORIGIN_USER= # usuário do novo ambiente
export ORIGIN_API=# api do novo ambiente. exemplo: http://localhost:8080/api/v4/projects
export ORIGIN_TOKEN=# token de acesso do novo ambiente (http://localhost/-/profile/personal_access_tokens)
```

3. Construindo imagem Docker:

```bash
docker build \
--build-arg SOURCE_ID=$SOURCE_ID \
--build-arg OLD_ORIGIN_USER=$OLD_ORIGIN_USER \
--build-arg OLD_ORIGIN_API=$OLD_ORIGIN_API \
--build-arg OLD_ORIGIN_TOKEN=$OLD_ORIGIN_TOKEN \ 
--build-arg ORIGIN_USER=$ORIGIN_USER \ 
--build-arg ORIGIN_API=$ORIGIN_API \
--build-arg ORIGIN_TOKEN=$ORIGIN_TOKEN \
-t gitlab-export .
```

4. Rodando em Docker:

```bash
docker run -it gitlab-export bash
```

5. Executando a migração:

```bash
python3 get-all.py && \
python3 post-all.py
```

6. Caso queira deletar todos os projetos:

```bash
python3 delete-projects.py
```