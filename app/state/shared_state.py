import flet as ft

# Refs usados em painéis como TopSummaryPanel
label_refs = {
    "metal": ft.Ref[ft.Text](),
    "cristal": ft.Ref[ft.Text](),
    "prometium": ft.Ref[ft.Text](),
    "energia": ft.Ref[ft.Text](),
    "horario": ft.Ref[ft.Text](),
    "tick": ft.Ref[ft.Text](),
    "mina_metal": ft.Ref[ft.Text](),
    "mina_cristal": ft.Ref[ft.Text](),
    "sint_prometium": ft.Ref[ft.Text](),
    "planta_solar": ft.Ref[ft.Text](),
    "planta_fusao": ft.Ref[ft.Text](),
}
tick_counter = {"value": 0}