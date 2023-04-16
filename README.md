# fattools

fattools contains scripts and tools to deal with '.csv' files in command line.
##### fattools is written in Python 3.

## Clone or download

```bash
git clone https://github.com/tigofat/fattools.git
```
## Usage

In the repo folder, configure `fat_config.json` file.

```bash
{
    "python_interpreter_name": "SAMPLE: python3 or python",
    "source_code_path": "SAMPLE: path/to/source/code"
}
```

Once you have done this, call from anywhere
```bash
source ./'path/to/fattools.sh' [OPTIONAL] config.json
```

Note: `config.json` can be any json file with required fields, but by default it will pass `fat_config.json` file. 
Please configure json file carefully, to not get unexpected errors.

### Example

```bash
$ source ./fattools.sh fat_config.json

OUTPUT:

Welcome to
   __           _     _             _       
  / _|         | |   | |           | |      
 | |_    __ _  | |_  | |_    ___   | |  ___ 
 |  _|  / _` | | __| | __|  / _ \  | | / __|
 | |   | (_| | | |_  | |_  | (_) | | | \__ \
 |_|    \__,_|  \__|  \__|  \___/  |_| |___/
 ```
 
 ```bash
 $ get_columns sample_data/sample.csv
 
 OUTPUT:
 
    id               value  
16407             98646.0  
16408             98680.0  
16409             98665.0  
16410            101061.0  
16411            112928.0  
16412            111935.0  
16413            111050.0  
16414            111515.0  
16415            104635.0  
  ...                 ...   
 7796            403100.0  
 7797            394403.0  
 7798            416720.0  
 7799            419116.0  
 7800            419332.0  
 7801            415981.0  
 7802            408619.0  
 7803            394613.0  
 7804            387594.0  
 7805            414123.0
 
 ```
 Note: The printing stype is changed when `stdin` is a terminal only.
 ```bash
 $ get_columns sample_data/sample.csv -c id value | apply '5*x + 1' 'x + 1'
 
 OUTPUT:
 
       id               value  
 82036.0             98647.0  
 82041.0             98681.0  
 82046.0             98666.0  
 82051.0            101062.0  
 82056.0            112929.0  
 82061.0            111936.0  
 82066.0            111051.0  
 82071.0            111516.0  
 82076.0            104636.0    
     ...                 ...   
 38981.0            403101.0  
 38986.0            394404.0  
 38991.0            416721.0  
 38996.0            419117.0  
 39001.0            419333.0  
 39006.0            415982.0  
 39011.0            408620.0  
 39016.0            394614.0  
 39021.0            387595.0  
 39026.0            414124.0
 ```

The sciprts also support `replace`, `append`, `concat` and `drop` operations on columns.
Do `operation_name -h` to find out about the operatoins in more detail.
