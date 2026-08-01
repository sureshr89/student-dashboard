with col_chart:
      st.markdown(
          f"<div style='text-align: center; color: #385b96; font-weight: bold;"
          f" margin-top: 10px;'>Improvement Trajectory</div>",
          unsafe_allow_html=True,
      )

      plot_df = (
          cat_df[["Test Name", "Total"]].copy()
          if "Total" in cat_df.columns
          else pd.DataFrame()
      )
      if not plot_df.empty:
        plot_df["Total"] = pd.to_numeric(plot_df["Total"], errors="coerce")
        plot_df = plot_df.dropna(subset=["Total"])

      if not plot_df.empty:
        fig = px.line(plot_df, x="Test Name", y="Total", markers=True)

        fig.update_xaxes(visible=False)
        fig.update_yaxes(
            title=None,
            showgrid=True,
            gridcolor="rgba(200, 200, 200, 0.3)",
            zeroline=False,
        )

        fig.update_layout(
            margin=dict(l=0, r=0, t=10, b=0),
            height=220,
            hovermode="x unified",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        # STATIC PLOT CONFIGURATION TO LOCK ZOOM/GESTURES
        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False,
                "staticPlot": (
                    True
                ),  # <- This completely removes all zoom, pan, and click gestures
            },
            theme="streamlit",
        )
      else:
        st.info("No valid test scores for trajectory.")
