import flet as ft

# Refs usados em painéis como TopSummaryPanel
label_refs = {
    "metal": ft.Ref[ft.Text](),
    "cristal": ft.Ref[ft.Text](),
    "prometium": ft.Ref[ft.Text](),
    "energia": ft.Ref[ft.Text](),
    "horario": ft.Ref[ft.Text](),
    "tick": ft.Ref[ft.Text](),
}
tick_counter = {"value": 0}