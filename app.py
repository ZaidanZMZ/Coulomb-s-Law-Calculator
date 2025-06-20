from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def format_number(value):
    """Format angka menjadi string biasa atau notasi ilmiah jika diperlukan"""
    if value == 0:
        return "0"
    
    # Jika nilai di antara 0.001 dan 1000, gunakan format desimal biasa
    if 0.001 <= abs(value) < 1000:
        # Format dengan 4 digit signifikan
        return f"{value:.6f}".rstrip('0').rstrip('.')
    
    # Gunakan notasi ilmiah untuk nilai sangat kecil atau besar
    exponent = math.floor(math.log10(abs(value)))
    coeff = value / (10 ** exponent)
    coeff_str = f"{coeff:.4f}".rstrip('0').rstrip('.')
    return f"{coeff_str} × 10^{exponent}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    mode = data['mode']
    inputs = data['inputs']
    
    # Konversi ke satuan dasar
    def convert_charge(value, unit):
        if unit == 'μC': return value * 1e-6
        if unit == 'nC': return value * 1e-9
        if unit == 'pC': return value * 1e-12
        return value
    
    q1 = convert_charge(inputs['q1_value'], inputs['q1_unit'])
    q2 = convert_charge(inputs['q2_value'], inputs['q2_unit'])
    r = inputs['distance_value']
    F = inputs.get('force_value', 0)
    k = float(inputs['constant_value'])
    
    # Format k untuk ditampilkan
    k_formatted = format_number(k)
    
    # Lakukan perhitungan
    result = {'unit': '', 'value': 0, 'formatted_value': '', 'steps': []}
    
    if mode == 'force':
        F_calculated = (k * abs(q1 * q2)) / (r * r)
        
        # Format khusus untuk gaya: angka biasa
        F_formatted = f"{F_calculated:.8f}".rstrip('0').rstrip('.')
        if '.' in F_formatted and len(F_formatted.split('.')[1]) > 4:
            F_formatted = f"{F_calculated:.4f}".rstrip('0').rstrip('.')
        
        result = {
            'value': F_calculated,
            'formatted_value': F_formatted,
            'unit': 'N',
            'formula': 'F = k · |q₁·q₂| / r²',
            'steps': [
                f"q₁ = {format_number(q1)} C",
                f"q₂ = {format_number(q2)} C",
                f"r = {r} m",
                f"k = {k_formatted} N·m²/C²",
                f"|q₁·q₂| = |{format_number(q1)} × {format_number(q2)}| = {format_number(abs(q1 * q2))}",
                f"r² = ({r})² = {r*r}",
                f"F = [{k_formatted} × {format_number(abs(q1 * q2))}] / {r*r}",
                f"F = {format_number(k * abs(q1 * q2))} / {r*r}",
                f"F = {F_formatted} N"
            ]
        }
    
    elif mode == 'distance':
        r_calculated = math.sqrt((k * abs(q1 * q2)) / F)
        result = {
            'value': r_calculated,
            'formatted_value': f"{r_calculated:.4f}",
            'unit': 'm',
            'formula': 'r = √(k · |q₁·q₂| / F)',
            'steps': [
                f"q₁ = {format_number(q1)} C",
                f"q₂ = {format_number(q2)} C",
                f"F = {F} N",
                f"k = {k_formatted} N·m²/C²",
                f"|q₁·q₂| = |{format_number(q1)} × {format_number(q2)}| = {format_number(abs(q1 * q2))}",
                f"k · |q₁·q₂| = {k_formatted} × {format_number(abs(q1 * q2))} = {format_number(k * abs(q1 * q2))}",
                f"k · |q₁·q₂| / F = {format_number(k * abs(q1 * q2))} / {F} = {format_number(k * abs(q1 * q2) / F)}",
                f"r = √({format_number(k * abs(q1 * q2) / F)})",
                f"r = {r_calculated:.4f} m"
            ]
        }
    
    elif mode == 'charge1' or mode == 'charge2':
        target = 'q₁' if mode == 'charge1' else 'q₂'
        other_charge = q2 if mode == 'charge1' else q1
        other_value = inputs['q2_value'] if mode == 'charge1' else inputs['q1_value']
        other_unit = inputs['q2_unit'] if mode == 'charge1' else inputs['q1_unit']
        other_symbol = 'q₂' if mode == 'charge1' else 'q₁'
        
        q_calculated = (F * (r * r)) / (k * abs(other_charge))
        
        # Tentukan tanda muatan berdasarkan input
        sign = -1 if (mode == 'charge1' and inputs['q1_value'] < 0) or (mode == 'charge2' and inputs['q2_value'] < 0) else 1
        q_calculated *= sign
        
        result = {
            'value': q_calculated,
            'formatted_value': format_number(q_calculated),
            'unit': 'C',
            'formula': f'{target} = (F · r²) / (k · |{other_symbol}|)',
            'steps': [
                f"F = {F} N",
                f"r = {r} m",
                f"k = {k_formatted} N·m²/C²",
                f"{other_symbol} = {format_number(other_charge)} C",
                f"r² = ({r})² = {r*r}",
                f"F · r² = {F} × {r*r} = {format_number(F * r * r)}",
                f"k · |{other_symbol}| = {k_formatted} × |{format_number(other_charge)}| = {format_number(k * abs(other_charge))}",
                f"{target} = {format_number(F * r * r)} / {format_number(k * abs(other_charge))}",
                f"{target} = {format_number(q_calculated)} C"
            ]
        }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)