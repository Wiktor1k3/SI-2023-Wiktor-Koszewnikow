import gradio as gr
import pandas as pd


def wyswietl_tabele(nazwa_pliku, wiersze, informacje_klasy_decyzyjnej):

    df = pd.read_csv(nazwa_pliku)
    liczba_wierszy, liczba_atrybutow= df.shape

    wiersze = int(wiersze)
    if wiersze > 0 and wiersze <= liczba_wierszy:
        tabela = df.head(wiersze)
    else:
        tabela = df

    liczba_obiektow, liczba_atrybutow = tabela.shape

    if informacje_klasy_decyzyjnej == "Liczba klas decyzyjnych":
        liczba_klas_decyzyjnych = len(tabela['Exited'].unique())
        opis_klasy_decyzyjnej = f"Liczba klas decyzyjnych: {liczba_klas_decyzyjnych}"
    elif informacje_klasy_decyzyjnej == "Wielkość każdej klasy decyzyjnej":
        wielkosc_klas_decyzyjnych = tabela['Exited'].value_counts().to_dict()
        opis_klasy_decyzyjnej = "Wielkość każdej klasy decyzyjnej: " + str(wielkosc_klas_decyzyjnych)
    else:
        opis_klasy_decyzyjnej = ""

    opis_tabeli = f'Tabela {nazwa_pliku} zawiera {liczba_obiektow} obiektów i {liczba_atrybutow} atrybutów.'
    opis_klasy = f'{opis_klasy_decyzyjnej}'

    return tabela, opis_tabeli, opis_klasy

interfejs = gr.Interface(
    fn=wyswietl_tabele,
    inputs=[
        gr.inputs.Textbox(label="Nazwa pliku CSV", default="Churn_Modelling.csv"),
        gr.inputs.Number(label="Liczba wyświetlanych wierszy", default=10),
        gr.inputs.Dropdown(label="Pytanie", choices=["Wielkość każdej klasy decyzyjnej", "Liczba klas decyzyjnych", ""],default="")

    ],
    outputs=[
        gr.outputs.Dataframe(label="Tabela", type='pandas'),
        gr.outputs.Textbox(label="Opis tabeli decyzyjnej"),
        gr.outputs.Textbox(label="Dodatkowe informacje:"),
    ],
    title="Interfejs do wyświetlania tabeli",
    description="Ten interfejs wyświetla wybrane wiersze z tabeli, a także zwraca opis tabeli decyzyjnej.",
)

interfejs.launch()
