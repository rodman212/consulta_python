import streamlit as st

# Dicionário com bibliotecas e suas principais funções em ordem alfabética
libraries = {
    "Listas": sorted([
        "all()", "any()", "append()", "clear()", "copy()", "count()", "enumerate()", "extend()", "index()", "insert()",
        "len()", "list()", "max()", "min()", "pop()", "remove()", "reverse()", "slice()", "sort()", "sum()"
    ]),
    "Loops": sorted([
        "break", "continue", "dict comprehension", "else", "enumerate()", "for", "for-else", "infinite loops", "iteration over dictionaries", "iteration over lists",
        "iteration over strings", "list comprehension", "nested loops", "nested loops with break", "pass", "range()", "set comprehension", "using range with step",
        "while", "while-else"
    ]),
    "Matplotlib": sorted([
        "annotate()", "bar()", "boxplot()", "figure()", "grid()", "hist()", "legend()", "pie()", "plot()", "savefig()",
        "scatter()", "show()", "subplot()", "title()", "xlabel()", "xlim()", "xticks()", "ylabel()", "ylim()", "yticks()"
    ]),
    "NumPy": sorted([
        "argmax()", "argmin()", "arange()", "array()", "concatenate()", "dot()", "exp()", "eye()", "full()", "linspace()",
        "log()", "mean()", "ones()", "random()", "reshape()", "round()", "sqrt()", "sum()", "transpose()", "zeros()"
    ]),
    "Pandas": sorted([
        "DataFrame()", "apply()", "describe()", "drop()", "dropna()", "fillna()", "groupby()", "head()", "iloc[]", "loc[]",
        "merge()", "pivot_table()", "read_csv()", "read_excel()", "reset_index()", "set_index()", "sort_values()", "tail()", "to_csv()", "to_excel()"
    ]),
    "PyAutoGUI": sorted([
        "PAUSE", "alert()", "click()", "confirm()", "dragRel()", "dragTo()", "hotkey()", "keyDown()", "keyUp()", "locateOnScreen()",
        "mouseDown()", "mouseUp()", "moveRel()", "moveTo()", "position()", "prompt()", "scroll()", "screenshot()", "size()", "typewrite()"
    ]),
    "Python": sorted([
        "abs()", "all()", "any()", "bin()", "bool()", "callable()", "chr()", "dir()", "divmod()", "enumerate()",
        "filter()", "float()", "format()", "getattr()", "hasattr()", "hash()", "hex()", "id()", "input()", "int()"
    ]),
    "Requests": sorted([
        "auth()", "content()", "cookies()", "delete()", "get()", "head()", "headers()", "history()", "json()", "options()",
        "params()", "patch()", "post()", "put()", "raise_for_status()", "session()", "status_code()", "text()", "timeout()", "url()"
    ]),
    "Selenium": sorted([
        "back()", "click()", "close()", "current_url", "execute_script()", "find_element()", "find_elements()", "forward()", "get()", "get_attribute()",
        "implicitly_wait()", "is_displayed()", "maximize_window()", "page_source", "quit()", "refresh()", "screenshot()", "send_keys()", "switch_to()", "title"
    ]),
    "Streamlit": sorted([
        "st.audio()", "st.button()", "st.checkbox()", "st.columns()", "st.dataframe()", "st.expander()", "st.file_uploader()", "st.form()", "st.image()", "st.markdown()",
        "st.metric()", "st.progress()", "st.radio()", "st.selectbox()", "st.sidebar()", "st.slider()", "st.table()", "st.text_input()", "st.video()", "st.write()"
    ]),
    "yfinance": sorted([
        "Ticker()", "actions", "balance_sheet", "calendar", "cashflow", "dividends", "download()", "earnings", "history()", "info",
        "institutional_holders", "major_holders", "options", "quarterly_balance_sheet", "quarterly_cashflow", "quarterly_earnings", "quarterly_financials", "recommendations",
        "splits", "sustainability"
    ]),
}

# Configurações da página
st.set_page_config(page_title="Consulta de Bibliotecas", layout="wide")

# Barra lateral para seleção da biblioteca
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
