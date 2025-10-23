# app_demo.py - VERSIÓN CORREGIDA Y OPTIMIZADA
import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Configuración de página
st.set_page_config(
    page_title="PanopticLabs - Inteligencia para MiPymes",
    page_icon="🎯",
    layout="wide"
)

def main():
    # Header principal
    st.title("🎯 PanopticLabs")
    st.markdown("### Inteligencia Cuantitativa para MiPymes de Veracruz")
    st.markdown("---")
    
    # Sidebar mejorado
    with st.sidebar:
        st.header("⚙️ Configura tu Análisis")
        
        industria = st.selectbox(
            "**Selecciona tu industria:**",
            ["Retail", "Restaurantes", "Servicios", "E-commerce", "Manufactura", "Turismo"]
        )
        
        tamaño = st.selectbox(
            "**Tamaño de empresa:**",
            ["Micro (1-10 empleados)", "Pequeña (11-50)", "Mediana (51-250)"]
        )
        
        presupuesto = st.slider(
            "**Presupuesto mensual en publicidad (MXN):**",
            min_value=2000, 
            max_value=50000, 
            value=15000, 
            step=1000
        )
        
        if st.button("🚀 Generar Análisis Personalizado", use_container_width=True):
            st.session_state.analisis_generado = True
            st.session_state.industria = industria
            st.session_state.presupuesto = presupuesto
    
    # Contenido principal
    if not st.session_state.get('analisis_generado', False):
        mostrar_landing_page()
    else:
        mostrar_analisis_completo(
            st.session_state.industria, 
            st.session_state.presupuesto
        )

def mostrar_landing_page():
    """Página de inicio del demo"""
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## 📊 Transforma Datos en Decisiones Rentables
        
        **En PanopticLabs ayudamos a MiPymes veracruzanas a:**
        
        ✅ **Identificar** campañas publicitarias más rentables  
        ✅ **Optimizar** presupuestos de marketing  
        ✅ **Reducir** costos de adquisición de clientes  
        ✅ **Aumentar** retorno de inversión (ROI)  
        ✅ **Tomar decisiones** basadas en datos, no en intuición  
        
        ### 🎯 Caso de Éxito Real
        *"Restaurante en Boca del Río identificó que el 65% de su presupuesto en Google Ads 
        generaba solo 20% de sus ventas. Reasignamos esos recursos a Instagram y 
        **aumentaron ventas 47% en 3 semanas**."*
        """)
    
    with col2:
        st.info("""
        **📈 Resultados Típicos**
        
        • **ROAS mejorado:** +40-60%
        • **CAC reducido:** -25-35%  
        • **Tiempo ahorrado:** 10-15h/semana
        • **Decisión más rápida:** 48h vs 2 semanas
        """)
    
    st.markdown("---")
    
    # Métricas de ejemplo
    st.subheader("🚀 Lo que Podrías Lograr")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("ROAS Mejorado", "+45%", "+152% vs industria")
    with col2:
        st.metric("Costo por Cliente", "-32%", "Ahorro mensual")
    with col3:
        st.metric("Tasa Conversión", "+28%", "Más ventas mismo presupuesto")
    with col4:
        st.metric("Tiempo de Análisis", "-85%", "Automatizado")
    
    st.markdown("""
    ---
    **👈 Usa la barra lateral para configurar y generar tu análisis personalizado gratuito**
    """)

def mostrar_analisis_completo(industria, presupuesto):
    """Análisis completo personalizado"""
    
    # Generar datos realistas
    datos = generar_datos_avanzados(industria, presupuesto)
    df = datos['df']
    
    # Header personalizado
    st.success(f"**📊 Análisis Personalizado para: {industria}**")
    st.write(f"**Presupuesto analizado:** ${presupuesto:,} MXN")
    
    # Métricas principales
    st.subheader("📈 Resumen Ejecutivo")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Inversión Total", f"${datos['gasto_total']:,.0f} MXN")
    
    with col2:
        st.metric("ROAS Promedio", f"{datos['roas_promedio']:.2f}x", "3.0x+ es óptimo")
    
    with col3:
        st.metric("CAC Promedio", f"${datos['cac_promedio']:.0f} MXN")
    
    with col4:
        st.metric("Campañas Optimizables", f"{datos['optimizables']}/{len(df)}")
    
    # Gráficos en columnas
    st.subheader("📊 Análisis Visual")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de ROAS
        fig_roas = px.bar(df, x='Campaña', y='ROAS', 
                         title='ROAS por Campaña',
                         color='ROAS', color_continuous_scale='RdYlGn')
        fig_roas.add_hline(y=2.0, line_dash="dash", line_color="red",
                          annotation_text="ROAS Mínimo Recomendado")
        fig_roas.update_layout(height=400)
        st.plotly_chart(fig_roas, use_container_width=True)
    
    with col2:
        # Gráfico de eficiencia
        fig_eficiencia = px.scatter(df, x='Gasto', y='ROAS', 
                                  size='Clientes', color='Campaña',
                                  title='Eficiencia: Gasto vs ROAS',
                                  hover_data=['CAC'])
        fig_eficiencia.update_layout(height=400)
        st.plotly_chart(fig_eficiencia, use_container_width=True)
    
    # Recomendaciones detalladas
    st.subheader("🎯 Recomendaciones Específicas")
    
    for _, campaña in df.iterrows():
        if campaña['ROAS'] > 3.0:
            st.success(f"""
            **✅ {campaña['Campaña']}** 
            - **ROAS:** {campaña['ROAS']:.2f}x (Excelente)
            - **CAC:** ${campaña['CAC']:.0f} MXN
            - **Recomendación:** Aumentar presupuesto en 20-30%
            """)
        elif campaña['ROAS'] > 2.0:
            st.warning(f"""
            **⚠️ {campaña['Campaña']}**
            - **ROAS:** {campaña['ROAS']:.2f}x (Aceptable)  
            - **CAC:** ${campaña['CAC']:.0f} MXN
            - **Recomendación:** Optimizar targeting y creativos
            """)
        else:
            st.error(f"""
            **❌ {campaña['Campaña']}**
            - **ROAS:** {campaña['ROAS']:.2f}x (Bajo)
            - **CAC:** ${campaña['CAC']:.0f} MXN  
            - **Recomendación:** Pausar y reestructurar campaña
            """)
    
    # Oportunidades de optimización
    st.subheader("💡 Oportunidades Identificadas")
    
    oportunidad_presupuesto = datos['gasto_total'] * 0.15  # 15% del presupuesto
    st.info(f"""
    **💰 Optimización de Presupuesto:**
    - **Presupuesto reasignable:** ${oportunidad_presupuesto:,.0f} MXN
    - **Campañas a reducir:** {len(df[df['ROAS'] < 1.5])}
    - **Campañas a escalar:** {len(df[df['ROAS'] > 2.5])}
    - **Potencial mejora ROAS:** +{(datos['roas_maximo'] - datos['roas_promedio']):.2f}x
    """)
    
    # Call to Action
    mostrar_cta_profesional()

def generar_datos_avanzados(industria, presupuesto):
    """Genera datos realistas basados en industria y presupuesto"""
    
    campañas = [
        'Facebook Ads', 
        'Google Search', 
        'Instagram',
        'Google Display', 
        'TikTok',
        'Facebook Leads'
    ]
    
    datos = []
    
    for campaña in campañas:
        # Ajustar según industria
        if industria == "Restaurantes":
            multiplicador_base = random.uniform(2.0, 5.0)
        elif industria == "Retail":
            multiplicador_base = random.uniform(1.8, 4.0)
        else:
            multiplicador_base = random.uniform(1.5, 3.5)
        
        gasto = random.randint(int(presupuesto*0.1), int(presupuesto*0.3))
        ventas = gasto * multiplicador_base
        roas = ventas / gasto
        clientes = int(gasto / random.randint(200, 800))
        cac = gasto / clientes if clientes > 0 else gasto
        
        datos.append({
            'Campaña': campaña,
            'Gasto': gasto,
            'Ventas': ventas,
            'ROAS': roas,
            'Clientes': clientes,
            'CAC': cac
        })
    
    df = pd.DataFrame(datos)
    
    return {
        'df': df,
        'gasto_total': df['Gasto'].sum(),
        'roas_promedio': df['ROAS'].mean(),
        'cac_promedio': df['CAC'].mean(),
        'optimizables': len(df[df['ROAS'] > 2.5]),
        'roas_maximo': df['ROAS'].max()
    }

def mostrar_cta_profesional():
    """Call to Action profesional"""
    
    st.markdown("---")
    
    st.subheader("🚀 ¿Listo para Implementar Estas Mejoras en tu Negocio?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **📊 Diagnóstico Gratuito Incluye:**
        
        • Análisis completo de tus campañas actuales
        • Identificación de oportunidades específicas  
        • Plan de acción personalizado en 48 horas
        • Recomendaciones accionables inmediatas
        • Sin compromiso a largo plazo
        """)
    
    with col2:
        st.markdown("**📅 Agenda tu Consulta 30min**")
        
        with st.form("lead_captura"):
            nombre = st.text_input("Nombre completo*")
            email = st.text_input("Email*")
            telefono = st.text_input("Teléfono")
            negocio = st.text_input("Nombre de tu negocio*")
            
            submitted = st.form_submit_button("📍 Agendar Consulta Gratuita")
            
            if submitted:
                if nombre and email and negocio:
                    st.success("""
                    **¡Perfecto! Te contactaremos en menos de 24 horas.**
                    
                    **Prepara para la consulta:**
                    • Acceso a Google Ads/Facebook Ads (si tienes)
                    • Datos de ventas últimos 3 meses
                    • 2-3 preguntas específicas que quieras resolver
                    """)
                else:
                    st.error("Por favor completa los campos obligatorios (*)")

if __name__ == "__main__":
    main()