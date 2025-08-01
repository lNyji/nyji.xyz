# nyji.xyz

> 🌐 [Veja o site ao vivo](https://nyji.xyz)


![Dev](https://img.shields.io/badge/estado-Em%20desenvolvimento-blue?style=for-the-badge&logo=code&logoColor=white)
![Status Backend](https://img.shields.io/badge/Backend-%E2%9A%A1%EF%B8%8F%20Em%20Progresso-yellow?style=for-the-badge)
![Status Frontend](https://img.shields.io/badge/Frontend-%F0%9F%94%A5%20Em%20Progresso-yellow?style=for-the-badge)
![Status API](https://img.shields.io/badge/API-%E2%9D%8C%20Parado-red?style=for-the-badge)
![Status Documentação](https://img.shields.io/badge/Documentação-%F0%9F%93%9D%20Em%20Planejamento-blue?style=for-the-badge)

---

## 🌟 Sobre o projeto

**nyji.xyz** é meu site pessoal e portfólio, também usado como "laboratório" de testes.  
Este repositório reúne o código do backend (API REST com Django) e do frontend (HTML/CSS/JS), organizados de forma modular e escalável.

O objetivo é centralizar minha presença digital e praticar tecnologias modernas de desenvolvimento web — do design estático até integrações dinâmicas com banco de dados e API.

---

## ✨ Funcionalidades

* 🌐 Linktree pessoal e portfólio de projetos
* 🎨 Tema claro/escuro com detecção automática
* 🧲 Calculadora interativa e minigames (Snake, Quiz) - *em progresso*
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
| **Frontend**   | HTML5, CSS3, JavaScript                       |
| **Backend**    | Python, Django, Django REST Framework         |
| **Banco**      | SQLite (dev), PostgreSQL (produção)           |
| **Hospedagem** | GitHub Pages (frontend), VPS/Render (backend) |
| **Domínio**    | Gerenciado via Cloudflare (`nyji.xyz`)        |

---

## 📂 Estrutura do projeto

```
nyji.xyz/
├── src/
│   ├── apps/
│   │   ├── core/                 # settings, urls, wsgi, etc.
│   │   ├── main/                 # app principal
│   │   ├── projetos/             # subdomínio nyji.xyz/projetos/
│   │   ├── sobre/                # subdomínio nyji.xyz/sobre/
│   │   └── manage.py
│   └── web/                      # versão estática original (legado)
│       ├── css/
│       ├── js/
│       └── html/
│
├── docs/                         # documentação adicional
│   ├── changelog.md
│   ├── roadmap.md
│   └── readme.md
│
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## 💻 Como rodar localmente

### ✅ Backend (Django)

```bash
git clone https://github.com/lNyji/nyji.xyz.git
cd nyji.xyz/src/apps

python -m venv ../../venv
source ../../venv/bin/activate       # Linux/macOS
# ou: ../../venv/Scripts/activate    # Windows

pip install -r ../../requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### ✅ Frontend (estático - legado)

```bash
cd nyji.xyz/src/web/html
# Abra o index.html no navegador
# Ou use Live Server (VSCode) para simular ambiente
```

---

## 🔧 Deploy

* **Frontend:** GitHub Pages + domínio personalizado (via Cloudflare)
* **Backend:** VPS, Render, Railway, ou similar
* **Recomendações:** configurar `.env`, segurança, HTTPS e backups

> 📄 Veja instruções detalhadas em `docs/readme.md`

---

## 📅 Changelog

Acompanhe todas as versões e mudanças em [`docs/changelog.md`](docs/changelog.md)

---

## 📋 Roadmap

| Etapa                  | Descrição                                                               |
| ---------------------- | ----------------------------------------------------------------------- |
| 🟢 Site Estático       | HTML, CSS, JavaScript puro, design responsivo                           |
| 🟡 Funcionalidades     | Temas, animações, minigames, buscas, contador de visitas via API        |
| 🔴 API REST com Django | Endpoints para projetos, contato, analytics, admin completo             |
| 🔵 Expansão            | Integração contínua, multilinguagem, login/admin frontend, SEO avançado |

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

Distribuído sob a licença [Apache 2.0](./LICENSE).

---

## 👤 Sobre

Feito com 💜 por **Gabriel "Nyji" Bezerra**

[![GitHub](https://img.shields.io/badge/GitHub-lNyji-181717?style=for-the-badge&logo=github)](https://github.com/lNyji)
[![Site](https://img.shields.io/badge/Site-nyji.xyz-000000?style=for-the-badge&logo=cloudflare)](https://nyji.xyz)
[![Email](https://img.shields.io/badge/Email-gabrielnyji@proton.me-8B89CC?style=for-the-badge&logo=protonmail)](mailto:gabrielnyji@proton.me)

