# Install dependencies as needed:
# pip install kagglehub[polars-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "D:\SEMESTER 7\BIG DATA\tugas2-abd-2026\data"

# Load the latest version
lf = kagglehub.load_dataset(
  KaggleDatasetAdapter.POLARS,
  "mrayyanshehzad/synthetic-retail-dataset-10-million-transactions",
  file_path,
  # Provide any additional arguments like
  # sql_query, polars_frame_type, or 
  # polars_kwargs.
  # See the documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpolars
)

print("First 5 records:", lf.collect().head())