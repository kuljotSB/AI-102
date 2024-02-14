 def run(data):
     data = json.loads(data)
     input_entry = defaultdict(list)
        
     for key, val in data.items():
             input_entry[key].append(decode_nan(val))
    
     data_frame_directory = create_dfd_from_dict(input_entry, schema_data)
     score_module = ScoreModelModule()
     result, = score_module.run(
         learner=model,
         test_data=DataTable.from_dfd(data_frame_directory),
         append_or_result_only=True)
     output = result.data_frame.values.tolist()
        
     return {
             "predicted_price": output[0][-1]
     }    
