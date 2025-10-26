# yaml
spec:
  template:
    spec:
      containers:
        - name: synergychat-api
          image: bootdotdev/synergychat-api:latest
          env:
            - name: API_PORT
              valueFrom:
                configMapKeyRef:
                  name: synergychat-api-configmap
                  key: API_PORT
