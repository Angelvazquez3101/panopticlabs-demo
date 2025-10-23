import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

class GeneradorDatosDemo:
    def __init__(self):
        self.campañas = [
            'Facebook_Verano_2025', 'Google_Search_Navidad', 
            'Instagram_Reels_Promo', 'Google_Display_Remarketing',
            'Facebook_Lead_Gen', 'TikTok_Video_Campaña'
        ]
        
    def generar_datos_publicidad(self):
        """Genera datos de publicidad realistas para el demo"""
        datos = []
        for campaña in self.campañas:
            gasto = random.randint(2000, 15000)
            impresiones = gasto * random.randint(15, 40)
            clics = int(impresiones * random.uniform(0.01, 0.05))
            conversiones = int(clics * random.uniform(0.02, 0.08))
            
            datos.append({
                'campaña': campaña,
                'gasto': gasto,
                'impresiones': impresiones,
                'clics': clics,
                'conversiones': conversiones,
                'fecha_inicio': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
            })
        
        return pd.DataFrame(datos)
    
    def generar_datos_ventas(self, df_ads):
        """Genera datos de ventas correlacionados con publicidad"""
        datos_ventas = []
        for _, row in df_ads.iterrows():
            if 'Facebook' in row['campaña']:
                multiplicador = random.uniform(2.5, 4.0)
            elif 'Google' in row['campaña']:
                multiplicador = random.uniform(1.8, 3.0)
            else:
                multiplicador = random.uniform(1.5, 2.5)
            
            monto_ventas = row['gasto'] * multiplicador
            clientes = int(row['conversiones'] * random.uniform(0.8, 1.2))
            
            datos_ventas.append({
                'campaña': row['campaña'],
                'monto_ventas': monto_ventas,
                'clientes_nuevos': clientes,
                'ticket_promedio': monto_ventas / max(1, clientes)
            })
        
        return pd.DataFrame(datos_ventas)