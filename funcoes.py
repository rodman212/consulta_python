import streamlit as st

# Dicionário com bibliotecas e suas principais funções
libraries = {
    "NumPy": [
        "array()", "linspace()", "reshape()", "mean()", "dot()", "arange()", "random()", "transpose()", "sum()", "argmax()",
        "argmin()", "zeros()", "ones()", "full()", "eye()", "sqrt()", "exp()", "log()", "round()", "concatenate()"
    ],
    "Pandas": [
        "DataFrame()", "read_csv()", "merge()", "groupby()", "pivot_table()", "iloc[]", "loc[]", "fillna()", "dropna()", "to_csv()",
        "read_excel()", "to_excel()", "describe()", "sort_values()", "head()", "tail()", "drop()", "set_index()", "reset_index()", "apply()"
    ],
    "Matplotlib": [
        "plot()", "scatter()", "bar()", "hist()", "show()", "subplot()", "title()", "xlabel()", "ylabel()", "legend()",
        "grid()", "figure()", "savefig()", "xlim()", "ylim()", "xticks()", "yticks()", "annotate()", "boxplot()", "pie()"
    ],
    "Requests": [
        "get()", "post()", "put()", "delete()", "head()", "patch()", "options()", "auth()", "timeout()", "raise_for_status()",
        "session()", "cookies()", "headers()", "params()", "json()", "text()", "content()", "status_code()", "url()", "history()"
    ],
    "PyAutoGUI": [
        "click()", "moveTo()", "typewrite()", "screenshot()", "locateOnScreen()", "dragTo()", "keyDown()", "keyUp()", "hotkey()", "position()",
        "size()", "scroll()", "mouseDown()", "mouseUp()", "moveRel()", "dragRel()", "alert()", "confirm()", "prompt()", "PAUSE"
    ],
    "Selenium": [
        "find_element()", "click()", "send_keys()", "get()", "quit()", "find_elements()", "get_attribute()", "switch_to()", "execute_script()", "back()",
        "forward()", "refresh()", "maximize_window()", "implicitly_wait()", "close()", "title", "current_url", "page_source", "screenshot()", "is_displayed()"
    ],
    "Yfinance": [
        "download()", "Ticker()", "history()", "info", "actions", "dividends", "splits", "cashflow", "balance_sheet", "earnings",
        "recommendations", "sustainability", "major_holders", "institutional_holders", "quarterly_balance_sheet", "quarterly_cashflow", "quarterly_earnings",
        "quarterly_financials", "calendar", "options"
    ],
    "Streamlit": [
        "st.write()", "st.sidebar()", "st.selectbox()", "st.button()", "st.file_uploader()", "st.slider()", "st.text_input()", "st.checkbox()", "st.radio()", "st.markdown()",
        "st.dataframe()", "st.table()", "st.progress()", "st.image()", "st.video()", "st.audio()", "st.columns()", "st.expander()", "st.form()", "st.metric()"
    ],
}

# Configurações da página
st.set_page_config(page_title="Consulta de Bibliotecas", layout="wide")

# Barra lateral para seleção da biblioteca
st.sidebar.title("Selecione a Biblioteca")
selected_library = st.sidebar.selectbox("Biblioteca", options=libraries.keys())

# Exibição das funções principais
st.title(f"Funções principais da biblioteca {selected_library}")
if selected_library in libraries:
    st.write("### Lista de funções:")
    for function in libraries[selected_library]:
        st.write(f"- `{function}`")

# Mensagem para adicionar novas bibliotecas
st.sidebar.markdown("---")
st.sidebar.write("Adicione mais bibliotecas ao código para expandir!")
