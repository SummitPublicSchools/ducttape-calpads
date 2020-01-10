## Introduction
`ducttape-calpads` is a tool for extracting/downloading data from CALPADS (the California Department of Education state student data tracking system). The functionality is housed under one class, `Calpads`. Once the user information is supplied, the instantiated object will have access to all the supported functionality.

## Calpads Object
After [installing the package](https://github.com/SummitPublicSchools/ducttape-calpads/blob/master/README.md), you can instantiate a Calpads object by importing it:
```python 
from ducttape_calpads.calpads import Calpads
```

Instantiating Calpads requires a few arguments:
- username
- password
- wait time
- hostname
- temp folder path

```python
c = Calpads('username@email.org',
            'password',
            10,
            'calpads.org',
            '../data/' #Make sure path exists already
            )
```
If you will be sharing your code, particularly through GitHub, there are more and less secure ways to pass in the login credentials. At Summit Public Schools, we have normed on using `.ini` configuration files and share templates as needed. We'll describe how that structure might look for you in another section. Otherwise, using the `getpass` module or hardcoding in the credentials will also work.

## Available Functionality
We currently support the following data extract functionality as methods on a `Calpads` object:
- `get_current_language_data`
- `request_extract` *and* `download_extract`
- `download_snapshot_report`

We work on providing strong docstrings for each method to guide usage, but it's sometimes helpful to see examples.

## Example Scripts
```python
#To download the 1.18 Snapshot as an Excel sheet
#You can slot this into a loop to parameterize and meet your automation needs.
c.download_snapshot_report('1234567', #The 7-Digit LEA code used in CALPADS
                            '1.18', #Most reports can be downloaded by referring to their report number. There are edge cases like the 8.1 EOY3 report. See docstrings.
                            academic_year='2019-2020',
                            dl_type='excel', 
                            snapshot_status='SELPA Approved',
                            temp_folder_name='save_my_downloads' #If you want to save the excel file to a folder within the instantiated temp folder path
                            )
```

```python
dl_folder = 'save_my_downloads'
list_cenr = []
list_done = []
cds_lea_values = {'awesome_lea': '1234567',
                'another_one': '7654321'}

#To download an extract, you have to first request it.
for lea_name, lea_code in cds_lea_values.items():
    if c.request_extract(lea_code,'cenr', academic_year='2019-2020'):
        print('successfuly requested for:', lea_name)
    else:
        print('failed request for:', lea_name)
            
for lea_name, lea_code in cds_lea_values.items():
    if lea_name not in list_done:
        df = c.download_extract(lea_code, 'cenr', temp_folder_name=dl_folder)
        list_cenr.append(df)
        list_done.append(lea_name)
        print('Done:', lea_name)

#If you have multiple LEAs in your account, you can download them using similar pattern as above and concat to get a single dataframe.
calpads_enrollments = pd.concat(list_cenr)
```

In keeping with `ducttape` style, methods will return dataframes of the data. This will work best with `.txt` or `.csv` files. Other file types may have unexpected behavior. (For instance, currently PDF snapshot downloads will return `None`.)
