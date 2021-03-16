#! bash
echo "Generating SWAGGER files from YANG files"
for file in $(find ./YANG/ -name '*.yang'); do
  outfile=`echo ${file##*/} | sed 's/yang/json/g'`;
  echo "Generating ${outfile} from ${file}"
  pyang --plugindir ../EAGLE/YangJsonTools -f swagger -p YANG/ ${file} -o OAS/${outfile} --generate-rpc=False;
done
