# PATP-StudyCall

- Sistema desenvolvido para o PATP do 2 semestre da faculade IDEAU em Pyqt5 e com crud com Mysql Connector para que estudantes consigam registar chamados de itens danificados na faculdade.
* melhoria recente: Automacao basica com PyAutoGui
---

##  Visão geral



* Sistema desktop em pyqt5 com crud com mysql connector para abrir chamados para itens danificados(ex: janela quebrada mesa quebrada,goteira,etc).
* Destinado a estudantes e professores para que consigam comunicar problemas a direcao de uma faculdade.


---

##  Funcionalidades principais

* Cadastro de chamados 
* Visualização de Chamados e filtros por status na parte de administrador.
* Persistencia de dados com banco de dados Mysql
* Interfaces desktop em pyqt5
* Login funcional
* Ldmin validado pelo id da instituicao cadastrada
* Automacao de testes basica com PyAutoGui



---

##  Tecnologias

* Linguagem: `Python` (`3.13+`)
* Frameworks / libs: `PyQt5` / `MySQL connector` /`PyAutoGui´
* Banco de dados:`MySQL`


---

##  Pré-requisitos

* Python 3.13+ instalado
* ter o pyqt5,PyautoGui e Mysql connector instalados
* Banco de dados(execute o arquivo .sql no seu workbench)
* Para executar o arquivo de testes,tenha um adm ja cadastrado no banco e coloque os dados de acesso na funcao onde a imagem passada e "email" ,mude pro email do seu adm cadastrado ,e onde a imagem passada e "senha" ,aletere pra senha do respectivo adm(a imagem sempre e o 1 parametro da funcao onde tem 2 parametros).

---



## Estrutura do projeto:


- PATP-StudyCall/
- ├─model/
- │  ├─ crud_banco.py
- │  ├─ chamado.py
- │  ├─ usuario.py
- │  ├─ adm_usuario.py
- │  └─instituicao.py
- ├─dados/ * aqui esta o arquivo.sql que voce ira executar antes de rodar a aplicacao
- ├─ view/
- │  ├─ ui/ * arquivos.ui das interfaces em pyqt5
- │  ├─ chamado_user.py
- │  ├─ chamado_adm.py
- │  ├─ assumir_chamado.py
- │  ├─ abrir_chamado.py
- │  ├─ tela_login.py
- │  ├─ inicio_log.py
- │  ├─ inicio_log_adm.py
- │  ├─ telaInicio.py
- │  ├─ tela_login_adm.py
- │  ├─ user.py
- │  ├─ admin.py
- │  └─ facul.py
- ├─ main.py
- └─README.md









---

##  Instalação (exemplo básico)

```bash
# clonar repositório
git clone https://github.com/ldm-code/PATP-StudyCall.git
cd PATP-StudyCall

# criar e ativar venv (Linux/macOS)
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
# python -m venv .venv
# .\.venv\Scripts\Activate.ps1

# instalar dependências
pip install PyQt5
pip install  mysql-connector-python
pip install PyAutoGui
pip install Pillow
pip install opencv-python
```
## 📬 Contato

* Autores: Leonardo De Moraes,Gabriel Antonio Tunello,Victor Antonio Biazin
* Meu Email: demoraesleonardo327@gmail.com
* Email de Victor: victbiazin@gmail.com
* Email de Gabriel: gabrieltunello06@gmail.com
---





