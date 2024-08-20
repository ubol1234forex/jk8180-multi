rm -rf set-miner-on
rm -rf set-mode

site='www.github.com'
until $(ping -q -c1 ${site} > /dev/null 2>&1)
do
    echo "${site} is unreachable. Retrying"
    # continue
done

echo "github online"

sleep 3s

n=0
   until [ $n -ge ]
   do
      git clone "https://github.com/ubol1234forex/set-miner-on.git" && break
      n=$[$n+1]
      sleep 1
   done

n=0
   until [ $n -ge ]
   do
      git clone "https://github.com/ubol1234forex/set-mode.git"
      n=$[$n+1]
      sleep 1
   done
sleep 3s

python3 main.py
