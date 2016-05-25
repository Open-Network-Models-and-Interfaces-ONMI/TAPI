#! bash
for file in $(find ../YANG/ -name *.yang); do
  outfile=`echo ${file##*/} | sed 's/yang/swagger/g'`;
  echo "Generating ${outfile} from ${file}"
  pyang -f swagger -p ../YANG ${file} -o ${outfile};
done
