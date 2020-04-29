from django.shortcuts import render
from django.views import View
import pandas as pd
import io
import pickle

from . import forms


# Create your views here.
class MainView(View):
    def get(self, request):
        context = {"form": forms.CSVUploadForm}

        return render(request, "analyzer/index.html", context)

    def post(self, request):
        form = forms.CSVUploadForm(request.POST, request.FILES)
        context = {"form": form}

        text = ""
        for chunk in request.FILES["csv_file"]:
            text += chunk.decode()

        df = pd.read_csv(io.StringIO(text))
        model = pickle.load(open("./assets/model_brief.sav", "rb"))
        cols = pickle.load(open("./assets/cols.pkl", "rb"))

        df_cut = df[cols]
        df_cut.fillna(0)
        df["応募数 合計"] = model.predict(df_cut)

        print(df[["お仕事No.", "応募数 合計"]])

        return render(request, "analyzer/index.html", context)
