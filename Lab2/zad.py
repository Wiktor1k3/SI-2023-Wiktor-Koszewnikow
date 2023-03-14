import gradio as gr
import pandas as pd


def wyswietl_tabele(nazwa_pliku, wiersze):

    df = pd.read_csv(nazwa_pliku)
    liczba_wierszy, liczba_atrybutow= df.shape

    wiersze = int(wiersze)
    if wiersze > 0 and wiersze <= liczba_wierszy:
        tabela = df.head(wiersze)
    else:
        tabela = df

    liczba_obiektow, liczba_atrybutow = tabela.shape
    liczba_klas = len(tabela['Exited'].unique())
    rozmiary_klas = tabela['Exited'].value_counts()

    opis_tabeli = f'Tabela {nazwa_pliku} zawiera {liczba_obiektow} obiektów i {liczba_atrybutow} atrybutów.'
    opis_tabeli2 = f'Ilość klas decyzyjnych: {liczba_klas}'
    opis_tabeli3 = f'Rozmiary klas: {rozmiary_klas.to_dict()}'
    return tabela, opis_tabeli, opis_tabeli2, opis_tabeli3

interfejs = gr.Interface(
    fn=wyswietl_tabele,
    inputs=[
        gr.inputs.Textbox(label="Nazwa pliku CSV", default="Churn_Modelling.csv"),
        gr.inputs.Number(label="Liczba wyświetlanych wierszy", default=10),
    ],
    outputs=[
        gr.outputs.Dataframe(label="Wynik", type='pandas'),
        gr.outputs.Textbox(label="Opis tabeli decyzyjnej"),
        gr.outputs.Textbox(label="Ilość klas decyzyjnych"),
        gr.outputs.Textbox(label="Rozmiary klas decyzyjnych"),
    ],
    title="Interfejs do wyświetlania tabeli",
    description="Ten interfejs wyświetla wybrane wiersze z tabeli, a także zwraca opis tabeli decyzyjnej.",
)

interfejs.launch()
