# Train a character-level multiplication-example model

out_dir = 'out_arith_999x9999'
eval_interval = 2000
eval_iters = 200
log_interval = 100 # don't print too too often

always_save_checkpoint = True

wandb_log = False # override via command line if you like
wandb_project = 'multiplication-char'
wandb_run_name = 'multiplication-mini-gpt'

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
max_iters = 8e6
lr_decay_iters = 8000000 # make equal to max_iters usually
min_lr = .5e-5 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially