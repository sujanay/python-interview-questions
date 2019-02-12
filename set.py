from __future__ import print_function

def main():
    st = {"a", "b", "c"}
    st.add("d")
    st.add("a")
    st.remove("a")
    st.add("f")
    st.add("b")
    st.remove("b")
    st.add("g")

    # print("original", st)
    # print("sorted",sorted(st))
    # print(reversed(sorted(st)))

    for s in reversed(sorted(st)):
        print(s, end='')

main()