#echo 'Running Freyr with no bootstrap...'

#python main.py --msg='Freyr with no bootstrap' --dirname='freyr_no_bootstrap' --freyr_mode=True --bootstrap_mode=False

#echo 'Running Freyr with bootstrap...'

#python main.py --msg='Freyr with bootstrap' --dirname='freyr_bootstrap' --freyr_mode=True --bootstrap_mode=True

#echo 'Running tool mode with no bootstrap...'
#
#python main.py --msg='Tool mode with no bootstrap' --dirname='tool_no_bootstrap' --freyr_mode=False --bootstrap_mode=False
#
#echo 'Running tool mode with bootstrap...'
#
#python main.py --msg='Tool mode with bootstrap' --dirname='tool_bootstrap' --freyr_mode=False --bootstrap_mode=True

#echo 'Running Freyr with outlines with no bootstrap...'
#
#python main.py --msg='Freyr with outlines and no bootstrap' --dirname='freyr_outlines_no_bootstrap' --freyr_mode=True --outlines_mode=True --bootstrap_mode=False
#
#echo 'Running Freyr with outlines with bootstrap...'
#
#python main.py --msg='Freyr with outlines and bootstrap' --dirname='freyr_outlines_no_bootstrap' --freyr_mode=True --outlines_mode=True --bootstrap_mode=True

echo 'Running tool mode v2 with no bootstrap...'

python main.py --msg='Tool mode v2 with no bootstrap' --dirname='tool_v2_no_bootstrap' --freyr_mode=False --bootstrap_mode=False

echo 'Running tool mode v2 with bootstrap...'

python main.py --msg='Tool mode v2 with bootstrap' --dirname='tool_v2_bootstrap' --freyr_mode=False --bootstrap_mode=True

echo 'All experiments are done running.'