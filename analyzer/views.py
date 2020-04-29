from django.shortcuts import render
from django.views import View
from django.http import FileResponse
import pandas as pd
import io
import pickle

from . import forms


# Create your views here.
class MainView(View):
    def get(self, request):
        context = {"form": forms.CSVUploadForm, "download_path": ""}

        return render(request, "analyzer/index.html", context)

    def post(self, request):
        form = forms.CSVUploadForm(request.POST, request.FILES)
        context = {"form": form}

        df = self.str_to_df(request.FILES["csv_file"])
        self.prediction(df)

        context["download_path"] = "./download"

        return render(request, "analyzer/index.html", context)

    def str_to_df(self, f):
        text = ""
        for chunk in f:
            text += chunk.decode()

        return pd.read_csv(io.StringIO(text))

    def prediction(self, df):
        model = pickle.load(open("/app/assets/model_brief.sav", "rb"))
        cols = pickle.load(open("/app/assets/cols.pkl", "rb"))

        df_cut = df[cols]
        df_cut.fillna(0)
        df["応募数 合計"] = model.predict(df_cut)

        df[["お仕事No.", "応募数 合計"]].to_csv("./media/prediction.csv", index=False)


class DownloadView(View):
    def get(self, request):
        return FileResponse(open("./media/prediction.csv", "rb"))
