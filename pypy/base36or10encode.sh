# shell 10进制转换36进制
read -p "like this lo:vCTN0.VC.   :" example
value=$(date +'%y%m%d')
result=""
base36="0123456789abcdefghijklmnopqrstuvwxyz"
while true; do
        result=${base36:((value%36)):1}${result}
        if [ $((value=${value}/36)) -eq 0 ]; then
                break
        fi
done
echo $example$result



