import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="PMFBY ANALYSIS",layout="wide")
df=pd.read_excel("C:\\Users\\dell\\Desktop\\PMFBY Taluka 18-23.xlsx")
#st.dataframe(df)

st.title("Year Wise Analysis of PMFBY Data 2018-2023")


st.sidebar.header("Please Select the District and Taluka:")
district=st.sidebar.multiselect("Select the district:",options=df["District Name"].unique())


df_selection1=df[(df["District Name"].isin(district))]
taluka=st.sidebar.multiselect("Select the taluka:",options=df_selection1["Taluka Name"].unique())
df_selection=df_selection1[(df_selection1["Taluka Name"].isin(taluka))]


xyz=df_selection[["Year","Total Applications"]]
fig1=px.bar(xyz,x="Year",y="Total Applications",title="<b>Total Application per Year<b>",text_auto=True)
fig1.update_traces(marker_color='green')
fig1.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
st.plotly_chart(fig1)
xyz.reset_index(drop=True,inplace=True)

fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[xyz.columns.tolist()]+xyz.values.tolist()
            
n_rows=len(xyz)
n_cols=len(xyz.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)


x_farmers=df_selection[["Year","Farmers"]]
fig2=px.bar(x_farmers,x="Year",y="Farmers",title="<b>Total Farmers per Year<b>",text_auto=True)
fig2.update_traces(marker_color='purple')
fig2.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsalmon",paper_bgcolor="lightsalmon")

st.plotly_chart(fig2)
x_farmers.reset_index(drop=True,inplace=True)
#st.dataframe(x_farmers)

fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_farmers.columns.tolist()]+x_farmers.values.tolist()
            
n_rows=len(x_farmers)
n_cols=len(x_farmers.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)



x_fa=df_selection[["Year","Farmers","Total Applications"]]
x_fa_melted=x_fa.melt(id_vars=["Year"],value_vars=["Farmers","Total Applications"],var_name='Category',value_name="Farmers and Applications")
fig3=px.bar(x_fa_melted,x="Year",y="Farmers and Applications",color='Category',title="<b>Total Farmers And Applications per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Farmers":"#ec7c34","Total Applications":"darkslateblue"})
fig3.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightskyblue",paper_bgcolor="lightskyblue")
st.plotly_chart(fig3)
x_fa.reset_index(drop=True,inplace=True)
#st.dataframe(x_fa)
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_fa.columns.tolist()]+x_fa.values.tolist()
            
n_rows=len(x_fa)
n_cols=len(x_fa.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_pr=df_selection[["Year","GP/Sum Insured"]]
x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].round(2))*100
fig4 = px.line(x_pr, x="Year", y="GP/Sum Insured",title="<b>Average Premium rate per Year<b>", text="GP/Sum Insured")
fig4.update_traces(textposition="bottom center")
fig4.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
st.plotly_chart(fig4)
x_pr.reset_index(drop=True,inplace=True)
#st.dataframe(x_pr)
x_pr["GP/Sum Insured"]=(x_pr["GP/Sum Insured"].astype("int64"))

fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_pr.columns.tolist()]+x_pr.values.tolist()
            
n_rows=len(x_pr)
n_cols=len(x_pr.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_cap=df_selection[["Year","Claim Against Premium"]]
x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].round(2))*100
fig5 = px.line(x_cap, x="Year", y="Claim Against Premium",title="<b>Claim Against Premium per Year<b>", text="Claim Against Premium")
fig5.update_traces(textposition="top center")
fig5.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightyellow",paper_bgcolor="lightyellow")
st.plotly_chart(fig5)
x_cap.reset_index(drop=True,inplace=True)
x_cap["Claim Against Premium"]=(x_cap["Claim Against Premium"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_cap.columns.tolist()]+x_cap.values.tolist()
            
n_rows=len(x_cap)
n_cols=len(x_cap.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_area=df_selection[["Year","Area Insured"]]
fig6=px.bar(x_area,x="Year",y="Area Insured",title="<b>Area Insured(in Ha.) per Year<b>",text_auto=True)
fig6.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="whitesmoke",paper_bgcolor="whitesmoke")
st.plotly_chart(fig6)
x_area.reset_index(drop=True,inplace=True)
x_area["Area Insured"]=(x_area["Area Insured"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_area.columns.tolist()]+x_area.values.tolist()
            
n_rows=len(x_area)
n_cols=len(x_area.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_sum=df_selection[["Year","Sum Insured (In Lac.)"]]
fig7=px.bar(x_sum,x="Year",y="Sum Insured (In Lac.)",title="<b>Sum Insured (In Lac.) per Year<b>",text_auto=True)
fig7.update_traces(marker_color='red')
fig7.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgoldenrodyellow",paper_bgcolor="lightgoldenrodyellow")
st.plotly_chart(fig7)
x_sum.reset_index(drop=True,inplace=True)
x_sum["Sum Insured (In Lac.)"]=(x_sum["Sum Insured (In Lac.)"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_sum.columns.tolist()]+x_sum.values.tolist()
            
n_rows=len(x_sum)
n_cols=len(x_sum.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_gross=df_selection[["Year","Gross Premium"]]
fig8=px.bar(x_gross,x="Year",y="Gross Premium",title="<b>Gross Premium(in Lac.) per Year<b>",text_auto=True)
fig8.update_traces(marker_color='brown')
fig8.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
st.plotly_chart(fig8)
x_gross.reset_index(drop=True,inplace=True)
x_gross["Gross Premium"]=(x_gross["Gross Premium"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_gross.columns.tolist()]+x_gross.values.tolist()
            
n_rows=len(x_gross)
n_cols=len(x_gross.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)


x_gs=df_selection[["Year","Gross Premium","Sum Insured (In Lac.)"]]
x_gs_melted=x_gs.melt(id_vars=["Year"],value_vars=["Gross Premium","Sum Insured (In Lac.)"],var_name='Category',value_name="Gross Premium and Sum Insured (In Lac.)")
fig9=px.bar(x_gs_melted,x="Year",y="Gross Premium and Sum Insured (In Lac.)",color='Category',title="<b>Gross Premium And Sum Insured (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"blue","Sum Insured (In Lac.)":"red"})
fig9.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightgreen",paper_bgcolor="lightgreen")
st.plotly_chart(fig9)
x_gs.reset_index(drop=True,inplace=True)
x_gs["Gross Premium"]=(x_gs["Gross Premium"].astype("int64"))
x_gs["Sum Insured (In Lac.)"]=(x_gs["Sum Insured (In Lac.)"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_gs.columns.tolist()]+x_gs.values.tolist()
            
n_rows=len(x_gs)
n_cols=len(x_gs.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)


x_gt=df_selection[["Year","Gross Premium","Total Claim Paid"]]
x_gt_melted=x_gt.melt(id_vars=["Year"],value_vars=["Gross Premium","Total Claim Paid"],var_name='Category',value_name="Gross Premium and Total Claim Paid")
fig10=px.bar(x_gt_melted,x="Year",y="Gross Premium and Total Claim Paid",color='Category',title="<b>Gross Premium And Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Gross Premium":"green","Total Claim Paid":"yellow"})
fig10.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightpink",paper_bgcolor="lightpink")
st.plotly_chart(fig10)
x_gt.reset_index(drop=True,inplace=True)

x_gt["Gross Premium"]=(x_gt["Gross Premium"].astype("int64"))
x_gt["Total Claim Paid"]=(x_gt["Total Claim Paid"].astype("int64"))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_gt.columns.tolist()]+x_gt.values.tolist()
            
n_rows=len(x_gt)
n_cols=len(x_gt.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

x_ts=df_selection[["Year","Total Claim Paid","MT+L+PH"]]
x_ts_melted=x_ts.melt(id_vars=["Year"],value_vars=["MT+L+PH","Total Claim Paid"],var_name='Category',value_name="Summation of Midterm,Localized,Post Harvest and Total Claim")
fig11=px.bar(x_ts_melted,x="Year",y="Summation of Midterm,Localized,Post Harvest and Total Claim",color='Category',title="<b>Summation of Midterm,Localized,Post Harvest and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"olive","MT+L+PH":"purple"})
fig11.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aliceblue",paper_bgcolor="aliceblue")
st.plotly_chart(fig11)
x_ts.reset_index(drop=True,inplace=True)
#x_ts["Gross Premium"]=(x_ts["Gross Premium"].astype("int64"))
#
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_ts.columns.tolist()]+x_ts.values.tolist()
            
n_rows=len(x_ts)
n_cols=len(x_ts.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)




x_ty=df_selection[["Year","Total Claim Paid","Yield Based"]]
x_ty_melted=x_ty.melt(id_vars=["Year"],value_vars=["Yield Based","Total Claim Paid"],var_name='Category',value_name="Yield Based and Total Claim Paid")
fig12=px.bar(x_ty_melted,x="Year",y="Yield Based and Total Claim Paid",color='Category',title="<b>Yield Based and Total Claim Paid (In Lac.) per Year<b>",barmode='group',text_auto=True,color_discrete_map={"Total Claim Paid":"red","Yield Based":"yellow"})
fig12.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="aqua",paper_bgcolor="aqua")
st.plotly_chart(fig12)
x_ty.reset_index(drop=True,inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[x_ty.columns.tolist()]+x_ty.values.tolist()
            
n_rows=len(x_ty)
n_cols=len(x_ty.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

xrevenue=df_selection[["Year","Revenue"]]
fig14=px.bar(xrevenue,x="Year",y="Revenue",title="<b>Total Revenue(in Lac.) per Year<b>",text_auto=True)
fig14.update_traces(marker_color='green')
fig14.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="blanchedalmond",paper_bgcolor="blanchedalmond")
st.plotly_chart(fig14)
xrevenue.reset_index(drop=True,inplace=True)
xrevenue["Revenue"]=(xrevenue["Revenue"].astype("int64"))
xrevenue["Revenue"]=(xrevenue["Revenue"].round(2))
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[xrevenue.columns.tolist()]+xrevenue.values.tolist()
            
n_rows=len(xrevenue)
n_cols=len(xrevenue.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

xprevented=df_selection[["Year","Prevented Sowing"]]
fig15=px.bar(xprevented,x="Year",y="Prevented Sowing",title="<b>Total Prevented Sowing(in Lac.) per Year<b>",text_auto=True)
fig15.update_traces(marker_color='green')
fig15.update_layout(yaxis=dict(showgrid=False),plot_bgcolor="lightsteelblue",paper_bgcolor="lightsteelblue")
st.plotly_chart(fig15)
xprevented.reset_index(drop=True,inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(3,2))


table_data=[xprevented.columns.tolist()]+xprevented.values.tolist()
            
n_rows=len(xprevented)
n_cols=len(xprevented.columns)
row_colors=[['w'] *n_cols for _ in range(n_rows+1)]
row_colors[0]=['#FFDDC1']*n_cols
ax.axis("off")
ax.axis("tight")
table=ax.table(cellText=table_data, cellColours=row_colors,loc="center", cellLoc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
#table.scale(1,1.3)
for col in range(n_cols):
    table.auto_set_column_width([col])
for key,cell in table.get_celld().items():
    cell.set_fontsize(8)
    row,col=key
    if row==0:
        cell.set_text_props(weight='bold')

st.pyplot(fig)

