if [[ "$(python3 -V)" =~ "Python 3" ]];
then
  echo "Python 3 is installed"
else
  sudo apt-get install python3
fi
if [[ "$(pip3 -V)" =~ "pip" ]];
then
  echo "PIP3 installed"
else
  sudo apt-get install python3-pip
fi