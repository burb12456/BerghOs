import pandas as pd
from RANDCLASS import said

# Load the CSV file into a DataFrame


def Style():
    global df
    df = pd.read_csv('Untitled.csv')
    bob = True

    def sort():
        global df
        Title = Ask[1:].strip() 
        try:
            
            sorted_df = df.sort_values(by=Title)
            df = sorted_df
        except KeyError:
            said(f"Column '{Title}' does not exist in the DataFrame.")
        except Exception as e:
            said(f"Error: {e}")


    def filter():
        global df
        Filtering = Ask[1:].strip()
        try:
            if '=' in Filtering:
                col, value = Filtering.split('=', 1)
                filtered_df = df[df[col.strip()] == value.strip()]
            elif '<' in Filtering:
                col, value = Filtering.split('<', 1)
                filtered_df = df[df[col.strip()].astype(float) < float(value.strip())]
            elif '>' in Filtering:
                col, value = Filtering.split('>', 1)
                filtered_df = df[df[col.strip()].astype(float) > float(value.strip())]
            else:
                filtered_df = df.filter(items=[Filtering]) 

                

            
            df = filtered_df  
        except KeyError:
            said(f"Column '{col.strip()}' does not exist in the DataFrame.")
        except ValueError:
            said("Ensure numeric columns contain valid numbers for comparison.")
        except Exception as e:
            said(f"Error: {e}")

    while bob == True:
        print(df)
        Ask = input('What do you want beruh: ').strip()
        if Ask[:1] == 's':
            sort()
        elif Ask[:1] == 'f':
            filter()
        elif Ask == 'e':
            df.to_csv('sorted_output.csv', index=False)
            said("DataFrame saved as 'sorted_output.csv'")
        elif Ask == 'c':
            df = pd.read_csv('Untitled.csv')
            said("DataFrame restored to its original state.")
        elif Ask == 'exit':
            bob = False
        else:
            said("Invalid command. Use 's' for sort, 'f' for filter, 'e' to export, or 'c' to restore.")
    
