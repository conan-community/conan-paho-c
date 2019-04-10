/*******************************************************************************
 * Copyright (c) 2012, 2017 IBM Corp.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * and Eclipse Distribution License v1.0 which accompany this distribution.
 *
 * The Eclipse Public License is available at
 *   http://www.eclipse.org/legal/epl-v10.html
 * and the Eclipse Distribution License is available at
 *   http://www.eclipse.org/org/documents/edl-v10.php.
 *
 * Contributors:
 *    Ian Craggs - initial contribution
 *******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "MQTTClient.h"

#define ADDRESS     "tcp://iot.eclipse.org:1883"

void connlost(void *context, char *cause)
{
    printf("\nConnection lost\n");
    printf("     cause: %s\n", cause);
}

int main(int argc, char* argv[])
{
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    int rc;
    int ch;
    time_t time_seed;
    int random;
    char client_id [24] = {0};

    srand((unsigned int) time(&time_seed));
    random = rand() % 100000;
    snprintf(client_id, sizeof(client_id), "conanpahoc%d", random);

    printf("Connecting client %s to address %s\n", client_id, ADDRESS);
    MQTTClient_create(&client, ADDRESS, client_id,
        MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;

    printf("Set callbacks\n");
    MQTTClient_setCallbacks(client, NULL, connlost, NULL, NULL);

    MQTTClient_destroy(&client);
    return rc;
}
