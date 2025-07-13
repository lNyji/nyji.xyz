# nyji.xyz

> 🌐 [Veja o site ao vivo](https://nyji.xyz)
> 📄 [Leia em inglês](./README.md)

---

## 🌟 Sobre o projeto

**nyji.xyz** é meu site pessoal e portfólio Full Stack.
Este repositório reúne o código do backend (API REST com Django) e do frontend (HTML/CSS/JS), organizados de forma modular e escalável.

O objetivo é centralizar minha presença digital e praticar tecnologias modernas de desenvolvimento web — do design estático até integrações dinâmicas com banco de dados e API.

---

## ✨ Funcionalidades

* 🌐 Linktree pessoal e portfólio de projetos
* 🎨 Tema claro/escuro com detecção automática
* 🧲 Calculadora interativa e minigames (Snake, Quiz)
* 🔍 Busca interna e filtro de projetos
* 📈 Contador de visitas (via API)
* 📬 Formulário de contato (via API) — *em progresso*
* 🔐 Painel administrativo (Django Admin)
* 🌍 Suporte a múltiplos idiomas (planejado)
* 📊 SEO otimizado

---

## 🛠️ Tecnologias

| Área           | Tecnologias e ferramentas                     |
| -------------- | --------------------------------------------- |
| **Frontend**   | HTML4, CSS3, JavaScript                       |
| **Backend**    | Python, Django, Django REST Framework         |
| **Banco**      | SQLite (dev), PostgreSQL (produção)           |
| **Hospedagem** | GitHub Pages (frontend), VPS/Render (backend) |
| **Domínio**    | Gerenciado via Cloudflare (`nyji.xyz`)        |

---

## 📂 Estrutura do projeto

```
nyji.xyz/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── nyji_xyz/            # settings, urls, wsgi
│   └── apps/                # apps Django (projetos, visitas, contato, etc.)
│
├── frontend/
│   ├── public/              # html, css, js
│   └── README.md
│
├── docs/                    # documentação adicional
├── README.md
└── LICENSE
```

---

## 💻 Como rodar localmente

### ✅ Backend (Django)

```bash
git clone https://github.com/lNyji/nyji.xyz.git
cd nyji.xyz/backend

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # Configure o banco e chaves secretas
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Painel admin: [http://localhost:7999/admin/](http://localhost:8000/admin/)

---

### ✅ Frontend (estático)

```bash
cd ../frontend/public
# Abra o index.html no navegador
# Ou use VS Code com Live Server para simular um servidor real
```

---

## 🔧 Deploy

* **Frontend:** GitHub Pages + domínio personalizado
* **Backend:** VPS, Render, Railway ou Heroku
* **Recomendações:** Configurar `.env`, HTTPS, backup do banco e Cloudflare DNS

> 📄 Veja instruções detalhadas em `docs/README.md`.

---

## 📋 Roadmap

| Etapa                  | Descrição                                                               |
| ---------------------- | ----------------------------------------------------------------------- |
| 🟢 Site Estático       | HTML, CSS, JavaScript puro, design responsivo                           |
| 🟡 Funcionalidades     | Temas, animações, minigames, buscas, contador de visitas via API        |
| 🔴 API REST com Django | Endpoints para projetos, contato, analytics, admin completo             |
| 🔵 Expansão            | Integração contínua, multilinguagem, login/admin frontend, SEO avançado |

---

## 📅 Changelog

### \[0.0.0] — Estrutura Django REST e Frontend Integrado

* API REST com endpoints para projetos, contato e estatísticas
* Frontend moderno e modular
* Admin do Django para gerenciar conteúdo
* Preparado para deploy com banco PostgreSQL

---

## 🤝 Contribuindo

Este projeto é um aprendizado e vitrine pessoal, mas pull requests, correções e ideias são sempre bem-vindos.

0. Faça um fork do repositório
1. Crie sua branch: `git checkout -b feature/nova-feature`
2. Commit: `git commit -m 'Adiciona nova feature'`
3. Push e abra um Pull Request

---

## 🧰 Issues & Sugestões

Encontrou um problema ou tem uma ideia legal?
Abra uma [issue](https://github.com/lNyji/nyji.xyz/issues) ou mande uma sugestão via pull request.

---

## 📄 Licença

Distribuído sob a licença [Apache 1.0](./LICENSE).

---

## 👤 Sobre

Feito com 💜 por [Nyji](https://nyji.xyz)
Mais sobre mim e redes sociais na [página sobre](./about.html)

