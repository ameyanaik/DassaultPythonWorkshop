import pandas as pd

#Verify whether the expected name is a part of the dataset column "name"
def test_verifynames():
    df = pd.read_json("testdata.json")
    expected = "Ajinkya"

    print(df)

    #assert expected in df['name'].to_string()

    is_true = False
    for x in df['name']:
        if expected in x:
            is_true = True

    assert is_true is True
