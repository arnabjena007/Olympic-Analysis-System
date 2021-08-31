#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CLASS:12
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#TOPIC:OLYMPICS DATA ANALYSIS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#IMPORTING LIBRARIES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as ts
import mysql.connector as sqlcn
#DATAFRAME USED
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df=pd.read_csv('olymp_data.csv')
pd.set_option('display.max_columns',None)

#FUNCTION FOR THE MAIN MENU
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
    ans=True
    while ans:
        print("""
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
OLYMPICS GAMES ANALYSIS SYSTEM
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1- Data Visualisation
2- Data Analysis
3- Read CSV/EXCEL File
4- Import / Export from/to MySQL
5- Data Manipulation
6- Exit
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
        inp=int(input("Enter your choice: "))
        if inp==1:
            datavisual()
        elif inp==2:
            odanalysis()
        elif inp==3:
            read_csv_excel()
        elif inp==4:
            imp_exp_sql()
        elif inp==5:
            manuplt()
        elif inp==6:
            ex=input("Are you sure you want to exit?(y/n)")
            if ex=='y' or ex=='Y':
                print(" Exiting now............Done! \nHave A Nice Day!!")
                sys.exit()
        else:
            print("\nInvalid Input Try again")
 


#FUNCTION FOR PLOTTING GRAPHS/CHARTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def datavisual():
    ans=True
    while ans:
        print('''
====================================
DATA VISUALISATION OF TOP 10 COUNTRIES
====================================
1- Line Chart~> COUNTRIES VS TOTAL MEDALS
2- Line Chart~> COUNTRIES VS TOTAL NO. OF TIMES PARTICIPATED (IN SUMMER & WINTER)
3- Bar Chart ~> COUNTRIES VS TOTAL NO. OF GOLD MEDALS
4- Bar Chart ~> COUNTRIES VS TOTAL NO. OF SILVER MEDALS
5- Bar Chart ~> COUNTRIES VS TOTAL NO. OF BRONZE MEDALS.
6- Pie Chart ~> DISTRIBUTION OF GOLD, SILVER & BRONZE MEDALS
7- Pie Chart ~> COUNTRY WISE GOLD, SILVER & BRONZE MEDALS
8- Bar Chart ~> COUNTRIES VS TOTAL NO. OF MEDALS (IN SUMMER AND WINTER)
9- Histogram ~> NO. OF COUNTRIES(GOLD, SILVER AND BRONZE MEDALS)
10- Exit to Main Menu
====================================
===================================''')
        ans=input("Please enter your choice:")
        if ans=='1':
            line_chart1()
        elif ans=='2':
            line_chart2()
        elif ans=='3':
            bar_chart1()
        elif ans=='4':
            bar_chart2()
        elif ans=='5':
            bar_chart3()
        elif ans=='6':
            pie_chart()
        elif ans=='7':
            pie_chart_country()
        elif ans=='8':
            dbargraph()
        elif ans=='9':
            dhistogm()
        elif ans=='10':
            menu()
        else:
            print("\nInvalid choice.Try again")
            continue


#TO PLOT LINE CHART--> TOP 10 COUNTRIES VS TOTAL MEDALS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def line_chart1():
    df=pd.read_csv('olymp_data.csv')
    df.sort_values(by='TotalMedal', ascending=False, inplace=True)
    df=df.loc[:,['Country','TotalMedal']]
    df1=df.head(10)
    Countries=df1['Country']
    Totalmedals=df1['TotalMedal']
    plt.plot(Countries,Totalmedals,linestyle=':',color='green',marker='.')
    x=np.arange(len(Countries))
    plt.xticks(x,Countries,rotation=30)
    plt.xlabel('Country~ ~ ~~~ >',fontsize=12,color='r')
    plt.ylabel('Total Medals~~~~>',fontsize=12,color='r')
    plt.title('TOTAL MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
    plt.show()
    

    
#TO PLOT LINE CHART --> TOP 10 COUNTRIES VS TOTAL NO. OF TIMES PARTICIPATED (IN SUMMER & WINTER)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def line_chart2():
    df=pd.read_csv('olymp_data.csv')
    df.sort_values(by='TotalTimesPart', ascending=False, inplace=True)
    df=df.loc[:,['Country','SummerTimesPart','WinterTimesPart' ]]
    df1=df.head(10)
    Countries=df1['Country']
    Stotal=df1['SummerTimesPart']
    Wtotal=df1['WinterTimesPart']
    plt.plot(Countries,Stotal,linestyle='dashed',color='orange',label='Summer',marker='+')
    plt.plot(Countries,Wtotal,linestyle='dashed',color='dimgrey',label='Winter',marker='+')
    x=np.arange(len(Countries))
    plt.xticks(x,Countries,rotation=30)
    plt.xlabel('Country~~~~>',fontsize=12,color='r')
    plt.ylabel('No. of times participated~~~~>',fontsize=12,color='r')
    plt.title('TOTAL NO. OF TIMES PARTICIPATED BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO, OF GOLD MEDALS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bar_chart1():
    df=pd.read_csv('olymp_data.csv')
    df=df.sort_values('Tgoldmedal',ascending=False)
    df1=df.head(n=10)
    x=np.arange(len(df1))
    Countries=df1['Country']
    totalgold=df1['Tgoldmedal']
    plt.bar(x+0.25, totalgold,width=.6, label='Total No. of Gold Medals by Top 10 Countries',color='gold')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Gold Medal Analysis of Top 10 Countries',color='blue',fontsize= 16)
    plt.xlabel('Countries~~~~~>',fontsize=12,color='red')
    plt.ylabel('No. of Gold Medals~~~~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF SILVER MEDALS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bar_chart2():
    df=pd.read_csv('olymp_data.csv')
    df=df.sort_values('Tsilvermedal',ascending=False)
    df1=df.head(n=10)
    x=np.arange(len(df1))
    Countries=df1['Country']
    totalsilver=df1['Tsilvermedal']
    plt.bar(x+0.25,totalsilver,width=.6, label='Total No. of Silver Medals by Top 10 Countries',color='silver')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Silver Medal Analysis of Top 10 Countries',color='blue',fontsize=16)
    plt.xlabel(' Countries ~ ~ ~~ ~ >',fontsize=12,color='red')
    plt.ylabel('No. of Silver Medals ~~~~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()


#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF BRONZE MEDALS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bar_chart3():
    df=pd.read_csv('olymp_data.csv')
    df=df.sort_values('Tbronzemedal',ascending= False)
    df1=df.head(n=10)
    x=np.arange(len(df1))
    Countries=df1['Country']
    totalbronze=df1['Tbronzemedal']
    plt.bar(x+0.25,totalbronze,width=.6,label='Total No. of Bronze Medals by Top 10 Countries',color='peru')
    plt.xticks(x,Countries,rotation=30)
    plt.title('Olympics Bronze Medal Analysis of Top 10 Countries',color='blue',fontsize=16)
    plt.xlabel('Countries~~~~~>',fontsize=12,color='red')
    plt.ylabel('No. of Bronze Medals~~~ ~~>',fontsize=12,color='red')
    plt.grid()
    plt.legend()
    plt.show()

#TO PLOT PIE CHART --> DISTRIBUTION OF MEDALS(GOLD,SILVER&BRONZE)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pie_chart():
    df=pd.read_csv('olymp_data.csv')
    df.sum(axis=0, skipna = True)
    lst=df.iloc[:,6:9].sum(axis=0)
    lst.values.tolist()
    clm=['Bronze','Silver','Gold']
    plt.title("Medals Distribution",color='navy')
    plt.pie(lst,labels=clm,autopct="%1.1f%%",colors=['brown','silver','gold'],shadow=True)
    plt.legend(loc='upper left')
    plt.show()

#TO PLOT PIE CHART --> DISTRIBUTION OF MEDALS(GOLD,SILVER&BRONZE) COUNTRY WISE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def pie_chart_country():
    df=pd.read_csv('olymp_data.csv')
    cntry=input("Enter name of a Country - : ")
    df=df.loc[df['Country']==cntry,['Tgoldmedal','Tsilvermedal','Tbronzemedal']]
    lst=df.iloc[0]
    lst=list(lst)
    clm=['Bronze','Silver','Gold']
    plt.title("Country-"+cntry+" Medals",color='navy')
    plt.pie(lst,labels=clm,autopct="%1.1f%%",colors=['brown','silver','gold'],shadow=True)
    plt.legend(loc='upper left')
    plt.show()

#TO PLOT BAR CHART-->TOP 10 COUNTRIES VS TOTAL NO. OF MEDALS(IN SUMMER & WINTER)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dbargraph():   
    df=pd.read_csv('olymp_data.csv')
    df.sort_values(by='TotalMedal' ,ascending=False,inplace=True)
    df1=df.head(n=10)
    x=np.arange(len(df1))
    Countries=df1['Country']
    Summermedal=df1 ['SummerTotal']
    Wintermedal=df1 ['WinterTotal']
    plt.bar(x-0.2,Summermedal,label='Total No. of Medals by Top 10 Countries IN SUMMER', width=0.4, color='orangered')
    plt.bar(x+0.2,Wintermedal,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.4, color= 'grey')
    plt.xticks(x,Countries,rotation=20)
    plt.title('Olympic Medal Analysis by Top 10 Countries',color='navy' ,fontsize= 16)
    plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
    plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
    plt.grid()
    plt.legend()
    plt.show()

#TO PLOT HISTOGRAM-->COUNTRIES GETTING GOLD, SILVER AND BRONZE IN A GIVEN RANGE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dhistogm():
        df=pd.read_csv('olymp_data.csv')
        s=df['Tsilvermedal']
        g=df['Tgoldmedal']
        b=df['Tbronzemedal']
        clm=['Bronze','Silver','Gold']
        plt.hist([b,s,g],rwidth=0.9,color=['brown','silver','gold'],label=clm)
        plt.title('Olympic Medal Analysis',color='navy' ,fontsize= 16)
        plt.xlabel('No. of Medals ~~~>',fontsize=12,color='r')
        plt.ylabel('No. of Countries ~~~>',fontsize=12,color='r')
        plt.grid() 
        plt.legend()
        plt.show()



#FUNCTION FOR ANALYSIS OF OLYMPICS DATA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def odanalysis():
    while True:
        print("<------------------------->")
        print('Data Frame Analysis')
        print("<------------------------->")
        mn='''1) To print Records of Top Countries in terms of  Total Medals won in Olympics.
2) To print  Records of Top Countries in terms of Total Gold Medals won in Olympics.
3) To print Records of Top Countries in terms of Total Silver Medals won in Olympics.
4) To print Records of Top Countries in terms of Total Bronze Medals won in Olympics.
5) To print Records of Bottom-most Countries in terms of Medal won in Olympics
6) To print the General Information about  the dataframe used for Analysis.
7) To Describe the Structure of the Dataframe used for analysis.
8) To print the Data of column specified by the User
9) To print Maximum value for each Column in the Dataframe.
10)To display Gold, Silver and Bronze medals won by a Specific Country" 
11)To go back to the main menu'''
        print(mn)
        x=int(input("Enter your choice : "))
        print("---------x-------------------x------------------x------------------x")
        df=pd.read_csv('olymp_data.csv')
        if x==1:
            df=df.sort_values('TotalMedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','TotalMedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor," records from DataFrame")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==2:
            df=df.sort_values('Tgoldmedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tgoldmedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of gold medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==3:
            df=df.sort_values('Tsilvermedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tsilvermedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of silver medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==4:
            df=df.sort_values('Tbronzemedal',ascending=False,ignore_index=True)
            df=df.loc[:,['Country','Tbronzemedal']]
            nor=int(input("Enter the number of records to be displayed : "))
            print("Top",nor,"records by total no. of bronze medals")
            print(df.head(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==5:
            df=df.sort_values('TotalMedal',ascending=False,ignore_index=True)
            nor=int(input("Enter the number of records to be displayed : "))
            df=df.loc[:,['Country','TotalMedal']]
            print("Bottom",nor,"records from the dataframe")
            print(df.tail(nor))
            print("---------x-------------------x------------------x------------------x")
        elif x==6:
            print("Information of the dataframe")
            print(df.info())
            print("---------x-------------------x------------------x------------------x")
        elif x==7:
            print("Describing the basic characteristics of the dataframe")
            print(df.describe())
            print("---------x-------------------x------------------x------------------x")
        elif x==8:
            print("Name of the columns~~>",df.columns)
            clm=eval(input("Enter the column names in a list"))
            print(df[clm])
            print("---------x-------------------x------------------x------------------x")
        elif x==9:
            print("Maximum value for each column")
            print(df.max())
            print("---------x-------------------x------------------x------------------x")
        elif x==10:
            print("Name of All countries participating in Olympics")
            print(df['Country'].values)
            cntry=eval(input("Enter name of a Country / Countries inthe form of list like - ['India']: "))
            print("Total Gold, Silver and Bronze Won by a Country/Countries :")
            for cnt in cntry:
                print(df.loc[df['Country']==cnt,['Country','Tgoldmedal','Tsilvermedal','Tbronzemedal']])
            print("---------x-------------------x------------------x------------------x")
        elif x==11:
            menu()
            break

#READING CSV FILE /EXCEL FILE AND DISPLAYING DATAFRAME
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_csv_excel():
    ans=True
    while ans:
        print('''1) Read CSV file and display DataFrame
        \n2) Read Excel File and Display Dataframe
        \n3) Press 3 to go back to main menu''')
        ans=int(input('Enter your choice:'))
        if ans==1:
            df=pd.read_csv('olymp_data.csv')
            print(df)
            print("Done!")
        elif ans==2:
            fname=input("Enter filename with PATH and EXTENSION(.xls/.xlsx) :")
            df=pd.read_excel(fname)
            print(df)
            print("Done!")
        elif ans==3:
            menu()


#IMPORTING AND EXPORTING DATA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def imp_exp_sql():
    while True:
        print("\n\n"+"*"*60)
        print("Data Transfer to/from MySQL")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('''1- Import from MySQL to create and display DataFrame\
        \n\n2- Export from DataFrame to mySQL\
        \n\n3- Press to go back''')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ans=int(input("Enter your choice:"))
        if ans==1:
            sql2df()
        elif ans==2:
            df2sql()
        elif ans==3:
            menu()
        else:
            print("Invalid Input Try Again ")


#IMPORTING DATA TO DATAFRAME FROM MYSQL
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sql2df():
    db_conn=sqlcn.connect(host='localhost',database='aiden',
                          user='Arnab Jena',password='arnabjena692003')
    fname=input("Enter the tablename: ")
    db_cursor=db_conn.cursor()
    qry="SELECT * FROM "+fname+""

    db_cursor.execute(qry)
    table_rows=db_cursor.fetchall()

    for x in table_rows:
        print(x)
    db_cursor.close()
    db_conn.close()
    print(".........Done!!")

#EXPORTING DATA FROM DATAFRAME TO MYSQL
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def df2sql():
    df=pd.read_csv('olymp_data.csv')
    df1=df.head(n=11)
    print(df1)
    db_conn=sqlcn.connect(host='localhost',database='aiden',
                          user='Arnab Jena',password='arnabjena692003')
    tblname=input("Enter the table name: ")
    db_cursor=db_conn.cursor()
    db_cursor.execute("SHOW TABLES LIKE '"+tblname+"'")
    if db_cursor.fetchone():
        db_cursor2=db_conn.cursor()
        db_cursor2.execute("DELETE from "+tblname)
        db_conn.commit()
        for rows,rs in df1.iterrows():
            Country=rs[0]
            SummerTimesPart=str(rs[1])
            SummerTotal=str(rs[2])
            WinterTimesPart=str(rs[3])
            WinterTotal=str(rs[4])
            TotalTimesPart=str(rs[5])
            Tbronzemedal=str(rs[6])
            Tsilvermedal=str(rs[7])
            Tgoldmedal=str(rs[8])
            TotalMedal=str(rs[9])
            qry2="INSERT INTO "+tblname+" values('"+Country+"',"+SummerTimesPart+",\
            "+SummerTotal+","+WinterTimesPart+","+WinterTotal+","+TotalTimesPart+",\
            "+Tbronzemedal+","+Tsilvermedal+","+Tgoldmedal+","+TotalMedal+")"
            db_cursor2.execute(qry2)
        db_conn.commit()
        db_cursor2.close()
        print(" Data transfer from dataframe to mysql -> SUCCESSFULL........!")

    else:
        qry3="CREATE TABLE "+tblname+" (Country varchar(20) ,SummerTimesPart int ,SummerTotal int,\
           WinterTimesPart int, WinterTotal int , TotalTimesPart int ,Tbronzemedal int,Tsilvermedal int,\
           Tgoldmedal int,TotalMedal int)"
        db_cursor2=db_conn.cursor()
        db_cursor2.execute(qry3)
        db_conn.commit()
        for rows,rs in df1.iterrows():
            Country=rs[0]
            SummerTimesPart=str(rs[1])
            SummerTotal=str(rs[2])
            WinterTimesPart =str(rs[3])
            WinterTotal=str(rs[4])
            TotalTimesPart =str(rs[5])
            Tbronzemedal =str(rs[6])
            Tsilvermedal =str(rs[7])
            Tgoldmedal=str(rs[8])
            TotalMedal =str(rs[9])
            qry2="INSERT INTO "+tblname+" values(' "+Country+" ',"+SummerTimesPart+",\
              "+SummerTotal+","+WinterTimesPart+","+WinterTotal+","+TotalTimesPart+",\
              "+Tbronzemedal+", "+Tsilvermedal+","+Tgoldmedal+","+TotalMedal+")"
            db_cursor.execute(qry2)
        db_conn.commit()
        db_conn.close()
        db_cursor.close()
        print(' Data transfer from dataframe to mysql -> SUCCESSFULL.......!!')


#MANIPULATION OF DATA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def manuplt():
    df=pd.read_csv('olymp_data.csv')
    ans=True
    while ans:
        print('''DATA MANIPULATION\n
~~~~~~~~~~~~~~~~~~
1) Inserting a Row
2) Deleting a Row
3) Inserting a Column
4) Deleting a Column
5) Renaming a Column
6) Exit to main menu''')
        ans=int(input("Enter your choice :"))
        pd.set_option('display.max_columns',None)

        
        if ans==1:
            print("Enter the input in following format:")
            col=df.columns
            print(col)
            lst=eval(input(" Enter the row values in list :"))
            sr=pd.Series(lst,index=col)
            row_df1=pd.DataFrame([sr])
            df=pd.concat([row_df1,df],ignore_index=True)
            print(df)
            print('Row Added Successfully!!')
            print('~'*30)
        elif ans==2:
            inp=int(input("Enter the row's index you want to be deleted :"))
            df1=df.drop(inp,axis=0)
            print("~"*30)
            print("Dataframe after row index no.",inp,"is deleted -->")
            print("~"*30)
            print(df1)
            print("~"*30)
        elif ans==3:
            pd.set_option('display.width', 500)
            pd.set_option('display.max_columns', None)
            clname=input("Enter tthe column name :")
            inp=int(input("Enter the column index no. \nWhere You Want to input the Column :"))
            df.insert(inp,clname,"Nan")
            print(df)
            print("~"*30)
        elif ans==4:
            pd.set_option('display.width', 500)
            pd.set_option('display.max_columns', None)
            print('DataFrame before deleting the column')
            print(df)
            inp=input("Column name you want to delete : ")
            df=df.drop(inp,axis=1)
            print("DataFrame after deleting the column",inp,":")
            print(df)
            print("~"*30)
        elif ans==5:
            pd.set_option('display.width', 500)
            pd.set_option('display.max_columns', None)
            print("~"*30)
            print("DataFrame before changing the column name/s")
            print("~"*30)
            print(df)
            oldcm=input("Enter the column name you want to rename :")
            newcm=input("Enter the new column name :")
            df=df.rename(columns={oldcm:newcm})
            print("~"*30)
            print("Dataframe after changing the column name/s")
            print("~"*30)
            print(df)
            print("~"*30)
        elif ans==6:
            print("Returning to main menu......Done!!")
            menu()

menu()
#<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END OF PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

