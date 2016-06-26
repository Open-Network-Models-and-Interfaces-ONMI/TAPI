#! bash
find ../UML/ -maxdepth 1 -name "*.uml" ! -name "*Model*" -exec cp -t project {} \;
node ../../EAGLEUmlYangTools/xmi2yang\ tool-v2.0/main.js
mv project/*.yang .
rm project/*
