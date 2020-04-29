from django.forms import Form, FileField


class CSVUploadForm(Form):
    csv_file = FileField(label="CSV")
