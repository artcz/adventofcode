                                                 #                                                  
                                              #  #  #                                               
                                                ###                                                 
                                               #####                                                
                                            ## ##### ##                                             
                                               #####                                                
                                                ###                                                 
                                              #  #  #                                               
                                                 #                                                  
(                                              lambda                                               
                                               s,ft,i:                                              
                                             (getattr(s                                             
                                            ,"setrecurs"                                            
                                           "ionlimit")(                                             
                                          2500), print( [                                           
                                         len([v for k, v in                                         
                                         ft.reduce(   lambda                                        
                                        #######......#######                                        
                                             prev, b: {                                             
                                           **prev, "G": {                                           
                                          **prev ["G"],  (                                          
                                         lambda a:lambda v:                                         
                                        a(a,v))(lambda s,arg                                        
                                       :((((arg[0],arg[1])if(                                       
                                      arg!=(500,0))else None)                                       
                                     if prev["p2"]else((arg[0],                                     
                                    arg[1])if arg[1]<prev["maxy"                                    
                                   ]else None))if((arg[0],arg[1]+                                   
                                  1)in prev['G']and(arg[0]-1,arg[1                                  
                                 ]+1)in prev['G']and(arg[0]+1,arg[1                                 
                                 #############........#############                                 
                                      ]+1)in prev['G'])or arg[                                      
                                     1]>=prev["maxy"]+1 else(s(                                     
                                    s,(arg[0]+0,arg[1]+1))if(arg                                    
                                   [0]+0,arg[1]+1)not in prev['G'                                   
                                  ]else(s(s,(arg[0]-1,arg[1]+1))if                                  
                                 (arg[0]-1,arg[1]+1)not in prev['G'                                 
                                ]else(s(s,(arg[0]+1,arg[1]+1))if(arg                                
                               [0]+1, arg[1]+1)not in prev['G']  else                               
                              (None,print(arg)))))))((500, 0)) if None                              
                              not in prev["G"]else None:"o"},},range(5*                             
                            10000),ft.reduce(lambda a,b:{**a,"maxy":max(                            
                           k[1]for k in a["G"].keys())},range(1),{"G":{(x                           
                           ##################..........##################                           
                             ,y):"#"for item in[[ tuple( map( int,  pos                             
                            .split(',')))  for pos in item]  for item in                            
                           [line.strip().split('->')   for line in  data.                           
                          splitlines()]]for m,n in zip(item,item[1:])for x                          
                          in range(min(m[0],n[0]),max(m[0],n[0])+1)for y in                         
                         range(min(m[1],n[1]),max(m[1],n[1])+1)},"p2":p2,}))                        
                       ["G"].items()if v=="o"and k is not None])+p2 for(data,                       
                      p2)in( (i, False),(i, True))])))(__import__("sys"),                           
                      __import__("functools"), open(0).read().strip())#########                     
                    ############################################################                    
                   ##############################################################                   
                  ################################################################                  
                 ##################################################################                 
                ####################################################################                
               ######################################################################               
              ########################################################################              
             ##########################################################################             
            ############################################################################            
            ################################............################################            
                    ############################################################                    
