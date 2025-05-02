import streamlit as st
import pandas as pd

# アプリケーションのタイトルを設定
st.title('Excelファイル比較アプリ')

st.write('2つのExcelファイルをアップロードして、内容が一致するか確認できます。')

# 1つ目のファイルのアップロード
uploaded_file1 = st.file_uploader("1つ目のExcelファイルを選択してください", type=['xlsx', 'xls'])

# 2つ目のファイルのアップロード
uploaded_file2 = st.file_uploader("2つ目のExcelファイルを選択してください", type=['xlsx', 'xls'])

# 比較ボタン
if st.button('ファイルを比較する'):
    # 両方のファイルがアップロードされているか確認
    if uploaded_file1 is not None and uploaded_file2 is not None:
        try:
            # ファイルを読み込む
            df1 = pd.read_excel(uploaded_file1)
            df2 = pd.read_excel(uploaded_file2)

            # ファイル名の表示（任意）
            st.write(f"ファイル1: {uploaded_file1.name}")
            st.write(f"ファイル2: {uploaded_file2.name}")

            # ファイルの内容を比較する
            # シンプルな比較：両方のDataFrameが完全に一致するかを確認
            if df1.equals(df2):
                st.success('🥳 2つのファイルは完全に一致します！')
            else:
                st.warning('🤔 2つのファイルは一致しません。')

                # どの部分が一致しないかを確認するための補助情報（例：行数や列数の違い）
                if len(df1) != len(df2):
                    st.info(f'行数が異なります: ファイル1は {len(df1)} 行、ファイル2は {len(df2)} 行です。')
                if len(df1.columns) != len(df2.columns) or not df1.columns.equals(df2.columns):
                     st.info('列の数または列名が異なります。')

                # さらに詳細な比較結果を表示することも可能ですが、
                # 今回はシンプルに一致しないことを伝えるのみとします。
                # もし一致しない具体的な箇所を表示したい場合は、後でコードを修正できます。

        except Exception as e:
            st.error(f'ファイルの読み込み中または比較中にエラーが発生しました: {e}')
    else:
        st.warning('比較するには、2つのファイルをアップロードしてください。')

# アプリケーションのフッター（任意）
st.markdown("---")
st.write("これはシンプルなExcel比較アプリです。")
