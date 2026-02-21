# Problem 5 — Load a FASTA file and store sequences in a dictionary where keys are headers and values are full sequences (combine multi-line sequences).
fasta_dict = {}
with open("C:/Users/Bigza/Downloads/fasta_example.txt", "r") as file:
    header = None
    
    for line in file:
        line = line.strip()
        
        if line.startswith(">"):
            header = line[1:]
            fasta_dict[header] = ""
        else:
            fasta_dict[header] += line
print(fasta_dict)

# Problem 6 — For each sequence in the FASTA dictionary, count occurrences of A, T, G, and C and store or print the nucleotide counts.
for key, value in fasta_dict.items():
    fasta_dict[key]= {
    "A" : value.count("A"),
    "T" : value.count("T"),
    "G" : value.count("G"),
    "C" : value.count("C")
    }
print(fasta_dict)

# Problem 7 — Scan each sequence and find all starting positions of the motif "ATG" using a sliding window approach.

fasta_dict = {}
with open("C:/Users/Bigza/Downloads/fasta_example.txt", "r") as file:
    header = None
    
    for line in file:
        line = line.strip()
        
        if line.startswith(">"):
            header = line[1:]
            fasta_dict[header] = ""
        else:
            fasta_dict[header] += line
for key, value in fasta_dict.items():
    positions = []
    for i in range(len(value)-2):
        if value[i:i+3] =="ATG":
            positions.append(int(i))
        
    fasta_dict[key]= {
        "positions" : positions
                }
print(fasta_dict)

# Problem 8 — Given a list of read lengths, filter reads ≥ 100 bp and report the number kept and the percentage kept (and/or removed).
reads = [150, 98 ,102 ,35, 250, 87]
filt_reads = []
for x in reads:
    if x >= 100:
        filt_reads.append(x)
print(filt_reads)
print("Reads kept:", len(filt_reads))
print("Percentage of Reads kept:", (len(filt_reads)/len(reads))*100, "%")

#Problem 8 — GC Content Per Sequence

fasta_dict = {}
with open("C:/Users/Bigza/Downloads/seq1_mock.txt", "r") as file:
    header = None

    for line in file:
        line = line.strip()
        
        if line.startswith(">"):
            header = line[1:]
            fasta_dict[header] = ""
        else:
            fasta_dict[header] += line
print(fasta_dict)

fasta_dict1 = fasta_dict.copy()
for key, item in fasta_dict.items():
    gc_per = round((fasta_dict[key].count("G") + fasta_dict[key].count("C"))/len(fasta_dict[key])*100,2)
    fasta_dict1[key] = gc_per
    
print(fasta_dict1)