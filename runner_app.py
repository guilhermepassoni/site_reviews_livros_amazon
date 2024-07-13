import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "pagina_principal.py"]
sys.exit(stcli.main())