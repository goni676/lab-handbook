
# Laboratory Handbook

## Commands
* Recovering Files from a Snapshot Using UNIX Command Line - [source](https://www.egr.msu.edu/decs/help-support/how-to/recovering_files_from_snapshot_using_unix_command_line)
  1. Go to the directory where you want the recovered file located after you recover it. Within this, and all directories, is a hidden directory called ".snapshot".
     This directory does not appear with "ls" using any options, but is accessible with "cd".
  2. `cd .snapshot`
  3. Type `ls` - You will see the hourly, nightly and weekly snapshot archives.
     To see the timestamps associated with the creation of each of the snapshots, type `ls -lu`.
* `vim`
   * To open a file in Vim: `vim filename`
   * Enter insert mode: Press `i` in normal mode to enter insert mode before the cursor.
     Now you will see --INSERT-- at the bottom of the screen.
   * Saving and Exiting:
      * `:w` - Save changes (write).
      * `:q` - Quit (close).
      * `:wq or :x` - Save and quit.
      * `:q!` - Quit without saving changes (force quit).

## Server installation
When a package or library is designed for Ubuntu or has an Ubuntu version available, we employ the following commands. Instead of <package>, we specify the actual package name.

```bash
  gdocker up
```
```bash
  apt-get -o APT::Sandbox::User=root update
```
```bash
  apt-get -o APT::Sandbox::User=root install <package>
```

## VCF | bcftools

 ### Installation
[How to install BCFTOOLS in any Linux Machine](https://www.youtube.com/watch?v=EJGz3yryrPo)
 ### Filter VCF files

```bash
  specific/elkon/gonicohen/bcftools-1.14/bcftools 
  view -S ^/specific/elkon/gonicohen/newfile.txt 
  /specific/elkon/gonicohen/SHEBA/SHEBA_Freeze_One.NF.vcf.gz > 
  /specific/elkon/gonicohen/SHEBA/filtered.vcf

```
* **view**: This is the subcommand of bcftools used to view, filter, or transform VCF/BCF files.
* **-S ^/specific/elkon/gonicohen/newfile.txt**: This option specifies a file (newfile.txt) containing a list of sample names to be excluded (^ is used as a negation). The samples listed in newfile.txt will not be included in the output.
* **/specific/elkon/gonicohen/SHEBA/SHEBA_Freeze_One.NF.vcf.gz**: This is the input VCF file in compressed format (vcf.gz).
* **> /specific/elkon/gonicohen/SHEBA/filtered.vcf**: This part redirects the filtered output to a new file (filtered.vcf) in the specified directory.

```bash
  cat filtered.vcf | awk '{if($1==17) print $0}' | grep 
  -e 43097280 -e 43097281 -e  43097282 -e 43097283 -e 43097284 -e 43097285
```
* **cat filtered.vcf**: This part of the command reads the contents of the filtered.vcf file and outputs it to the standard output.
* **awk '{if($1==17) print $0}'**: This part of the command uses awk to filter lines where the value in the first column ($1) is equal to 17. It prints the entire line ($0) for those matching lines.
* **grep -e 43097280 -e 43097281 -e 43097282 -e 43097283 -e 43097284 -e 43097285**: This part of the command uses grep to further filter the output. It selects lines that contain any of the specified patterns (43097280, 43097281, 43097282, 43097283, 43097284, or 43097285).

```bash
  gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | head -48 | tail -1 | wc
```
* **head -48**: This part of the command uses the head command to display the first 48 lines of the uncompressed VCF file.
* **tail -1**: This part of the command uses the tail command to select the last line from the previously displayed 48 lines.
* **wc**: This part of the command uses the wc (word count) command to count the number of lines, words, and characters in the output.

## VEP

### installation

[Download and install](http://www.ensembl.org/info/docs/tools/vep/script/vep_download.html)

* #### **OSError: mysql_config not found:** 
  [(source)](https://github.com/JudgeGirl/Judge-sender/issues/4)
  
  Please be aware that it is necessary to adapt the `sudo` commands to Docker syntax, considering aspects such as sandboxing and the usage of `apt-get`. 
  ```bash
    sudo apt-get install mysql
  ```
  ```bash
    sudo apt-get install libmysqlclient-dev
  ```
  ```bash
    sudo apt-get install libmariadbclient-dev
  ```
  changes in /.bashrc:

  ```bash
  export PERL5LIB=$PERL5LIB:$HOME/cpanm/lib/perl5
  export KENT_SRC=$PWD/kent-335_base/src
  export MACHTYPE=$(uname -m)
  export CFLAGS="-fPIC"
  export MYSQLINC="mysql_config --include | sed -e 's/^-I//g'"
  export MYSQLLIBS="mysql_config --libs"
  export PERL5LIB=$PERL5LIB:$HOME/cpanm/lib/perl
  export PERL5LIB=${PERL5LIB}:/specific/elkon/gonicohen/ensembl-vep
  export PERL5LIB=${PERL5LIB}:/specific/elkon/gonicohen/ensembl-vep/Bio/DB/HTS
  alias vep="/specific/elkon/gonicohen/ensembl-vep/vep"
  ```
  *
  -------------------- EXCEPTION --------------------
  MSG: ERROR: Cache directory /root/.vep/homo_sapiens not found
### Running

```bash
/specific/elkon/sapir2/Lina_project/chr19/chr19_to_vep.vcf -o 
/specific/elkon/sapir2/Lina_project/chr19/chr19_after_vep.vcf --cache --dir_cache 
/specific/elkon/sapir2/ensembl-vep2 --fields "Allele,Consequence,IMPACT,SYMBOL,
Gene,Feature_type,Feature,BIOTYPE,EXON,INTRON,Protein_position,Amino_acids,
Codons,Existing_variation,DISTANCE,STRAND,FLAGS" &
```

