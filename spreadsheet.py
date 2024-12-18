import pandas as pd
from RANDCLASS import said

def Style():
    global df
    erd = 0

    bob = True
    while erd == 0:
        Ask = input('What stylesheet: ').strip()

        try:
            df = pd.read_csv(Ask + '.csv')
            global main_path
            main_path = Ask + '.csv'
            erd = 1
        except FileNotFoundError:
            said("File doesn't exist lol;")
        except Exception as e:
            said(f"Error: {e}")

    def sort():
        global df
        Title = Ask[1:].strip()
        try:
            sorted_df = df.sort_values(by=Title)
            df = sorted_df
            said(f"Sorted by column '{Title}'.")
        except KeyError:
            said(f"Column '{Title}' does not exist in the DataFrame.")
        except Exception as e:
            said(f"Error: {e}")

    def filter():
        global df
        tru = Ask[1:].strip()
        Filtering = tru.split(' ')
        print(Filtering)

        try:
            if '=' in tru:
                col, value = tru.split('=', 1)
                col = col.strip()
                filtered_df = df[df[col] == value.strip()]
            elif '<' in tru:
                col, value = tru.split('<', 1)
                col = col.strip()
                filtered_df = df[df[col].astype(float) < float(value.strip())]
            elif '>' in tru:
                col, value = tru.split('>', 1)
                col = col.strip()
                filtered_df = df[df[col].astype(float) > float(value.strip())]
            else:
                filtered_df = df.filter(items=Filtering)

            df = filtered_df
            said(f"Filtered by condition: {tru}")
        except KeyError:
            said(f"Column '{col}' does not exist in the DataFrame.")
        except ValueError:
            said("Ensure numeric columns contain valid numbers for comparison.")
        except Exception as e:
            said(f"Error: {e}")

    def export():
        check = Ask[1:].strip()
        df.to_csv(check + '.csv', index=False)
        said('Saved as ' + check + '.csv')

    def openStylesheet():
        global main_path, df
        check = Ask[1:].strip()
        main_path = check + '.csv'
        try:
            df = pd.read_csv(main_path)
            said('Opened new style sheet called ' + main_path)
        except FileNotFoundError:
            said('Directory not found')
        except Exception as e:
            said(f"Error: {e}")

    def create():
        global df
        check = Ask[1:].strip()
        tcheck = check.split(' ')
        tcheck2 = df.columns.tolist()

        if len(tcheck) == len(tcheck2):
            new_row = {tcheck2[i]: tcheck[i] for i in range(len(tcheck))}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            said("New row added successfully!")
        else:
            said('Column count mismatch. Could not add row.')

    def delete():
        global df
        tru = Ask[1:].strip()
        try:
            if '=' in tru:
                col, value = tru.split('=', 1)
                col = col.strip()
                df = df[df[col] != value.strip()]
                said(f"Deleted rows where {col} equals {value}.")
            else:
                said("Invalid delete condition. Use 'col=value'.")
        except KeyError:
            said(f"Column '{col}' does not exist in the DataFrame.")
        except Exception as e:
            said(f"Error: {e}")

    while bob:
        print(df)
        Ask = input('What do you want beruh: ').strip()

        if Ask[:1] == 's':
            sort()
        elif Ask[:1] == 'f':
            filter()
        elif Ask[:1] == 'e':
            export()
        elif Ask[:1] == 'c':
            create()
        elif Ask == 'z':
            df = pd.read_csv(main_path)
            said("FILE RESTORED!!!!!!!")
        elif Ask == 'GETMEOUT':
            bob = False
            said('darkside you are!!!!!')
        elif Ask[:1] == 'o':
            openStylesheet()
        elif Ask[:1] == 'd':
            delete()
        else:
            said(".lungepunch")
