import streamlit as st

# Dicionário com bibliotecas e suas funções (prioridade por uso nas funções)
libraries = {
    "Listas": [
        "append()", "pop()", "remove()", "insert()", "sort()", "reverse()", "extend()", "index()", "count()", "clear()",
        "len()", "max()", "min()", "sum()", "list()", "slice()", "copy()", "enumerate()", "any()", "all()"
    ],
    "Loops": [
        "for", "while", "break", "continue", "range()", "enumerate()", "nested loops", "for-else", "while-else", "list comprehension",
        "dict comprehension", "set comprehension", "pass", "iteration over lists", "iteration over dictionaries", "iteration over strings",
        "nested loops with break", "using range with step", "infinite loops", "else"
    ],
    "Matplotlib": [
        "plot()", "scatter()", "bar()", "hist()", "show()", "xlabel()", "ylabel()", "legend()", "title()", "grid()",
        "savefig()", "xlim()", "ylim()", "figure()", "xticks()", "yticks()", "subplot()", "pie()", "annotate()", "boxplot()"
    ],
    "NumPy": [
        "array()", "reshape()", "linspace()", "arange()", "mean()", "dot()", "sum()", "transpose()", "zeros()", "ones()",
        "full()", "eye()", "random()", "sqrt()", "log()", "exp()", "argmax()", "argmin()", "concatenate()", "round()"
    ],
    "Pandas": [
        "DataFrame()", "read_csv()", "head()", "tail()", "groupby()", "merge()", "pivot_table()", "iloc[]", "loc[]", "describe()",
        "fillna()", "dropna()", "drop()", "sort_values()", "reset_index()", "set_index()", "to_csv()", "read_excel()", "to_excel()", "apply()"
    ],
    "PyAutoGUI": [
        "click()", "moveTo()", "dragTo()", "screenshot()", "locateOnScreen()", "typewrite()", "keyDown()", "keyUp()", "hotkey()", "position()",
        "size()", "mouseDown()", "mouseUp()", "moveRel()", "dragRel()", "scroll()", "prompt()", "alert()", "confirm()", "PAUSE"
    ],
    "Python": [
        "print()", "input()", "len()", "int()", "str()", "float()", "abs()", "all()", "any()", "round()",
        "enumerate()", "filter()", "map()", "zip()", "sorted()", "range()", "bin()", "hex()", "chr()", "dir()"
    ],
    "Requests": [
        "get()", "post()", "put()", "delete()", "raise_for_status()", "timeout()", "auth()", "json()", "text()", "status_code()",
        "options()", "patch()", "head()", "session()", "cookies()", "headers()", "params()", "content()", "url()", "history()"
    ],
    "Selenium": [
        "get()", "find_element()", "send_keys()", "click()", "get_attribute()", "is_displayed()", "maximize_window()", "refresh()", "back()", "quit()",
        "find_elements()", "switch_to()", "execute_script()", "forward()", "implicitly_wait()", "page_source", "title", "current_url", "close()", "screenshot()"
    ],
    "Streamlit": [
        "st.write()", "st.selectbox()", "st.button()", "st.slider()", "st.text_input()", "st.checkbox()", "st.radio()", "st.markdown()", "st.sidebar()", "st.file_uploader()",
        "st.dataframe()", "st.table()", "st.progress()", "st.image()", "st.video()", "st.audio()", "st.columns()", "st.expander()", "st.form()", "st.metric()"
    ],
    "yfinance": [
        "download()", "Ticker()", "history()", "info", "actions", "dividends", "splits", "cashflow", "balance_sheet", "earnings",
        "recommendations", "sustainability", "major_holders", "institutional_holders", "quarterly_balance_sheet", "quarterly_cashflow", "quarterly_earnings",
        "quarterly_financials", "calendar", "options"
    ],
}

# Configurações da página
st.set_page_config(page_title="Consulta de Bibliotecas", layout="wide")

# Barra lateral para seleção da biblioteca (em ordem alfabética)
st.sidebar.title("Selecione a Biblioteca")
selected_library = st.sidebar.selectbox("Biblioteca", options=sorted(libraries.keys()))

# Exibição das funções principais
st.title(f"Funções principais da biblioteca {selected_library}")
if selected_library in libraries:
    st.write("### Lista de funções:")
    for function in libraries[selected_library]:
        st.write(f"- `{function}`")

# Mensagem para adicionar novas bibliotecas
st.sidebar.markdown("---")
st.sidebar.write("Adicione mais bibliotecas ao código para expandir!")
