from analise_atendimentos import periodo, interesse, df

def test_conversao():
    assert periodo(10) == "Manhã"
    assert periodo(13) == "Tarde"
    assert periodo(21) == "Noite"

def test_total_atendimento():
    assert len(df) > 0