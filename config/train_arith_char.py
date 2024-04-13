# train a miniature character-level shakespeare model
# good for debugging and playing on macbooks and such

out_dir = 'out-arith-char'
eval_interval = 2000
eval_iters = 200
log_interval = 100 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'shakespeare-char'
wandb_run_name = 'mini-gpt'

dataset = 'arith_char'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = .5e-4
#max_iters = 50000 --- this took about 1/2 hour
# Specify enought iters for 50000 * 40 = 2,000,000 or about 20 hours (if running at that same iters per hour)
max_iters = 2000000
lr_decay_iters = 50000 # make equal to max_iters usually
min_lr = .5e-5 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only
# compile = False # do not torch compile the model
