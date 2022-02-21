const Like = (field: OperatorLike['field'], value: OperatorLike['value']): OperatorLike => {
    return {
      type: "Like",
      field,
      value,
    };
  };
  
  export default Like;
  