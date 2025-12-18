import json
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# BASE DE DADOS COMPLETA EXTRAÍDA DOS SEUS ARQUIVOS
dados_app = {
    "Natal": [
        {"id": 1, "equip": "FACILE 110", "cliente": "JOSE ANTONIO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 2, "equip": "FACILE 110", "cliente": "LAUDIO", "pilsen": 70, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 3, "equip": "FACILE 110", "cliente": "MAICON", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 4, "equip": "FACILE 110", "cliente": "ARIOVALDO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 5, "equip": "FACILE 110", "cliente": "CECILIA (FERN.)", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 6, "equip": "FACILE 110", "cliente": "LARANI (FERN.)", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 7, "equip": "FACILE 110", "cliente": "MARIA CLARA (FERN.)", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 8, "equip": "FACILE 110", "cliente": "BRUNO", "pilsen": 80, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 9, "equip": "FACILE 220", "cliente": "GONÇALO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 10, "equip": "FACILE 220", "cliente": "IVAN", "pilsen": 60, "escuro": 10, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 11, "equip": "FACILE 220", "cliente": "IAGO (FERN.)", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 12, "equip": "FACILE 220", "cliente": "ANDERSON", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "Já Pagou", "entrega": "Pendente"},
        {"id": 13, "equip": "MINE 110", "cliente": "IVAN", "pilsen": 60, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 14, "equip": "MINE 110", "cliente": "JOSE CARLOS", "pilsen": 30, "escuro": 0, "puro_malte": 30, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 15, "equip": "MINE 110", "cliente": "VLADIMIR", "pilsen": 0, "escuro": 0, "puro_malte": 80, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 16, "equip": "MAX", "cliente": "RODRIGO BAIO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 17, "equip": "MAX", "cliente": "MARCEL", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 18, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 19, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 20, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 21, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 22, "equip": "MAX TAP", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 23, "equip": "MINE 220 TAP", "cliente": "RAQUEL", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 24, "equip": "MINE 220", "cliente": "GISELE GRANJA", "pilsen": 0, "escuro": 10, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 25, "equip": "GELO", "cliente": "ARNALDO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"}
    ],
    "Ano_Novo": [
        {"id": 101, "equip": "FACILE 110", "cliente": "NELSON", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 102, "equip": "FACILE 110", "cliente": "ALANA", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 103, "equip": "FACILE 110", "cliente": "ARIOVALDO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 104, "equip": "FACILE 110", "cliente": "LAUDIO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 105, "equip": "FACILE 110", "cliente": "DANIELE", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 106, "equip": "FACILE 110", "cliente": "JOSLENE", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 107, "equip": "FACILE 110", "cliente": "RONY", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 108, "equip": "FACILE 110", "cliente": "THALES", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 109, "equip": "FACILE 220", "cliente": "ELIAS", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "Já Pagou", "entrega": "Pendente"},
        {"id": 110, "equip": "FACILE 220", "cliente": "TANIA", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "Já Pagou", "entrega": "Pendente"},
        {"id": 111, "equip": "FACILE 220", "cliente": "SUELI", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "Já Pagou", "entrega": "Pendente"},
        {"id": 112, "equip": "FACILE 220", "cliente": "MAURICIO", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 113, "equip": "MINE 110", "cliente": "ERICA", "pilsen": 100, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 114, "equip": "MINE 110", "cliente": "JOEL", "pilsen": 100, "escuro": 0, "puro_malte": 0, "status": "Já Pagou", "entrega": "Pendente"},
        {"id": 115, "equip": "MINE 110", "cliente": "JESSICA", "pilsen": 50, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 116, "equip": "MAX", "cliente": "CAMILA FERNANDES", "pilsen": 200, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 117, "equip": "MAX", "cliente": "VITOR HUGO", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 118, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 119, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 120, "equip": "MAX", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 121, "equip": "MAX TAP", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"},
        {"id": 122, "equip": "MINE 220 TAP", "cliente": "", "pilsen": 0, "escuro": 0, "puro_malte": 0, "status": "A Pagar", "entrega": "Pendente"}
    ]
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Germania Fernandópolis</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #f39c12; --bg: #0f172a; --surface: #1e293b;
            --text: #f8fafc; --success: #10b981; --danger: #ef4444;
        }
        * { box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 10px; }
        .container { max-width: 1200px; margin: auto; }

        header { text-align: center; padding: 15px 0; border-bottom: 2px solid var(--primary); margin-bottom: 20px; }
        header h1 { font-size: 1.4rem; color: var(--primary); margin: 0; text-transform: uppercase; }

        /* DASHBOARD RESPONSIVO */
        .dashboard { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; margin-bottom: 20px; }
        .stat-card { background: var(--surface); padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #334155; }
        .stat-label { font-size: 0.7rem; color: #94a3b8; text-transform: uppercase; font-weight: bold; }
        .stat-value { font-size: 1.6rem; font-weight: 700; display: block; margin-top: 5px; }

        .tabs { display: flex; gap: 8px; margin-bottom: 15px; }
        .tab { flex: 1; text-align: center; padding: 12px; background: var(--surface); text-decoration: none; color: #94a3b8; border-radius: 8px; font-weight: bold; font-size: 0.9rem; border: 1px solid #334155; }
        .tab.active { background: var(--primary); color: #000; border-color: var(--primary); }

        /* TABELA RESPONSIVA */
        .table-wrapper { background: var(--surface); border-radius: 12px; overflow-x: auto; box-shadow: 0 4px 15px rgba(0,0,0,0.4); }
        table { width: 100%; border-collapse: collapse; min-width: 850px; }
        th { background: #111827; padding: 12px; color: var(--primary); font-size: 0.7rem; text-transform: uppercase; text-align: center; }
        td { padding: 10px; border-bottom: 1px solid #334155; text-align: center; }

        .row-available { background: rgba(243, 156, 18, 0.12); }
        input, select { background: #0f172a; border: 1px solid #444; color: white; padding: 8px; border-radius: 6px; font-size: 0.85rem; width: 100%; }
        input[type="number"] { width: 60px; text-align: center; font-weight: bold; color: var(--primary); }
        
        .btn-save { background: var(--primary); color: #000; border: none; padding: 10px; border-radius: 6px; font-weight: 700; width: 100%; cursor: pointer; }
        .btn-add { background: var(--success); color: white; border: none; padding: 15px; border-radius: 10px; font-weight: bold; width: 100%; margin-top: 20px; cursor: pointer; }
        
        @media (max-width: 600px) {
            body { padding: 5px; }
            .stat-value { font-size: 1.3rem; }
            th, td { padding: 8px 5px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Germania / Votuporanga e Fernandópolis</h1>
        </header>

        <div class="dashboard">
            <div class="stat-card">
                <span class="stat-label">Frota</span>
                <span class="stat-value">{{ total }}</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">Ocupadas</span>
                <span class="stat-value" style="color: var(--danger);">{{ ocupadas }}</span>
            </div>
            <div class="stat-card">
                <span class="stat-label">Livres</span>
                <span class="stat-value" style="color: var(--success);">{{ disponiveis }}</span>
            </div>
        </div>

        <div class="tabs">
            <a href="/?aba=Natal" class="tab {{ 'active' if aba_ativa == 'Natal' }}">🎄 NATAL</a>
            <a href="/?aba=Ano_Novo" class="tab {{ 'active' if aba_ativa == 'Ano_Novo' }}">🎆 ANO NOVO</a>
        </div>

        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th style="width: 130px;">Equipamento</th>
                        <th>Cliente</th>
                        <th>Pilsen</th>
                        <th>Escuro</th>
                        <th>Malte</th>
                        <th style="width: 130px;">Financeiro</th>
                        <th style="width: 130px;">Entrega</th>
                        <th style="width: 80px;">Ação</th>
                    </tr>
                </thead>
                <tbody>
                    {% for item in lista %}
                    <tr class="{{ 'row-available' if not item.cliente else '' }}">
                        <form action="/atualizar" method="POST">
                            <input type="hidden" name="aba" value="{{ aba_ativa }}">
                            <input type="hidden" name="id" value="{{ item.id }}">
                            <td><strong style="color: var(--primary); font-size: 0.8rem;">{{ item.equip }}</strong></td>
                            <td><input type="text" name="cliente" value="{{ item.cliente }}" placeholder="DISPONÍVEL"></td>
                            <td><input type="number" name="pilsen" value="{{ item.pilsen }}"></td>
                            <td><input type="number" name="escuro" value="{{ item.escuro }}"></td>
                            <td><input type="number" name="puro_malte" value="{{ item.puro_malte }}"></td>
                            <td>
                                <select name="status" style="color: {{ 'var(--success)' if item.status == 'Já Pagou' else 'var(--primary)' }}">
                                    <option value="A Pagar" {{ 'selected' if item.status == 'A Pagar' }}>💰 A PAGAR</option>
                                    <option value="Já Pagou" {{ 'selected' if item.status == 'Já Pagou' }}>✅ PAGO</option>
                                </select>
                            </td>
                            <td>
                                <select name="entrega">
                                    <option value="Pendente" {{ 'selected' if item.entrega == 'Pendente' }}>🚚 PENDENTE</option>
                                    <option value="Realizada" {{ 'selected' if item.entrega == 'Realizada' }}>🏠 ENTREGUE</option>
                                </select>
                            </td>
                            <td><button type="submit" class="btn-save">OK</button></td>
                        </form>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <form action="/adicionar" method="POST" style="margin-top: 20px; background: var(--surface); padding: 15px; border-radius: 12px; border: 1px dashed var(--primary);">
            <input type="hidden" name="aba" value="{{ aba_ativa }}">
            <input type="text" name="novo_equip" placeholder="Nome do novo equipamento..." required style="margin-bottom: 10px;">
            <button type="submit" class="btn-add">➕ ADICIONAR AO INVENTÁRIO</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    aba = request.args.get('aba', 'Natal')
    lista = dados_app[aba]
    total = len(lista)
    disponiveis = len([i for i in lista if not i['cliente']])
    ocupadas = total - disponiveis
    return render_template_string(HTML_TEMPLATE, aba_ativa=aba, lista=lista, 
                                   total=total, disponiveis=disponiveis, ocupadas=ocupadas)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    aba = request.form.get('aba')
    idx = int(request.form.get('id'))
    item = next((i for i in dados_app[aba] if i['id'] == idx), None)
    if item:
        item.update({
            'cliente': request.form.get('cliente'),
            'pilsen': int(request.form.get('pilsen') or 0),
            'escuro': int(request.form.get('escuro') or 0),
            'puro_malte': int(request.form.get('puro_malte') or 0),
            'status': request.form.get('status'),
            'entrega': request.form.get('entrega')
        })
    return redirect(url_for('index', aba=aba))

@app.route('/adicionar', methods=['POST'])
def adicionar():
    aba = request.form.get('aba')
    novo_equip = request.form.get('novo_equip')
    novo_id = max([i['id'] for i in dados_app[aba]]) + 1 if dados_app[aba] else 1
    dados_app[aba].append({
        "id": novo_id, "equip": novo_equip, "cliente": "", 
        "pilsen": 0, "escuro": 0, "puro_malte": 0, 
        "status": "A Pagar", "entrega": "Pendente"
    })
    return redirect(url_for('index', aba=aba))

if __name__ == '__main__':
    app.run(debug=True)
