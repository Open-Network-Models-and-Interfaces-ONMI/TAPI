#! bash
echo "Generating TREE & SWAGGER files from YANG files"
for file in $(find ./YANG/ -name '*.yang'); do
  treefile=`echo ${file##*/} | sed 's/yang/tree/g'`;
  echo "Generating ${treefile} for ${file}"
  pyang --lint --strict -f tree -p YANG/ ${file} -o YANG/${treefile};
done
