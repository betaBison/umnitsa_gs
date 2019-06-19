# source umnitsa setup and set environment variables
umni(){
   source ~/Documents/umnitsa/devel/setup.bash
   export ROS_MASTER_URI=http://umnitsa.local:11311
   export ROS_HOSTNAME=$(hostname).local
}
