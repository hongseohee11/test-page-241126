import math
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title="Hypotenuse Calculator", page_icon="📐")
st.title("📐 빗변 계산기")
st.write("직각삼각형의 두 변(밑변, 높이)을 입력하면 빗변의 길이와 모형(그림)을 보여줍니다.")


col1, col2 = st.columns(2)
with col1:
    a = st.number_input("밑변 (a)", min_value=0.0, value=3.0, step=0.1, format="%.3f")
    b = st.number_input("높이 (b)", min_value=0.0, value=4.0, step=0.1, format="%.3f")
with col2:
    show_formula = st.checkbox("공식 보기 (피타고라스)", value=True)
    show_plot = st.checkbox("그림 보기", value=True)

if a == 0 and b == 0:
    st.info("적어도 하나의 변 길이를 0보다 크게 입력하세요.")
else:
    c = math.hypot(a, b)
    st.subheader("결과")
    st.metric("빗변의 길이 (c)", f"{c:.6f}")

    if show_formula:
        st.latex(r"c = \sqrt{a^2 + b^2}")
        st.write(f"a={a:.3f}, b={b:.3f} 이므로 c = {c:.6f}")

    if show_plot:
        # Create a simple right triangle with legs a and b
        fig, ax = plt.subplots()
        # triangle points: (0,0), (a,0), (0,b)
        xs = [0, a, 0, 0]
        ys = [0, 0, b, 0]
        ax.plot(xs, ys, marker="o")
        # annotate points
        ax.text(0, 0, "  O (0,0)", verticalalignment="bottom")
        ax.text(a, 0, f"  A ({a:.2f},0)", verticalalignment="bottom")
        ax.text(0, b, f"  B (0,{b:.2f})", verticalalignment="bottom")
        # annotate sides
        mid_ab = (a / 2, 0)
        mid_ob = (0, b / 2)
        mid_oa = (a / 3, b / 3)
        ax.annotate(f"a={a:.2f}", xy=mid_ab, xytext=(5, -10), textcoords="offset points")
        ax.annotate(f"b={b:.2f}", xy=mid_ob, xytext=(-50, 0), textcoords="offset points")
        ax.annotate(f"c={c:.2f}", xy=mid_oa, xytext=(5, 5), textcoords="offset points")
        ax.set_aspect("equal", adjustable="box")
        # set limits with a margin
        margin = max(a, b) * 0.15 if max(a, b) > 0 else 1
        ax.set_xlim(-margin, a + margin)
        ax.set_ylim(-margin, b + margin)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("직각삼각형 모형")
        st.pyplot(fig)

st.caption("입력한 두 변으로 피타고라스 정리를 사용해 빗변을 계산합니다.")
