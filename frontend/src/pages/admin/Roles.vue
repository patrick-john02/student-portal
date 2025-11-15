<script lang="ts">
export const description = "Roles management page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu"

import { Plus, MoreHorizontal, Users } from "lucide-vue-next"
const userRole = "Admin"

// Dummy roles data
const roles = ref([
  {
    id: 1,
    name: "Administrator",
    description: "Full system access and permissions.",
    users: 12,
    color: "bg-red-500",
  },
  {
    id: 2,
    name: "Teacher",
    description: "Access to teaching materials and student analytics.",
    users: 65,
    color: "bg-blue-500",
  },
  {
    id: 3,
    name: "Registrar",
    description: "Manages student records and documents.",
    users: 8,
    color: "bg-green-500",
  },
  {
    id: 4,
    name: "Finance",
    description: "Handles payments and financial reports.",
    users: 4,
    color: "bg-yellow-500",
  },
])

const search = ref("")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />


    <SidebarInset>
      <!-- Page Header -->
      <header
        class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all"
      >
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Roles</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Top Bar -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Roles</h2>
            <p class="text-sm text-muted-foreground">
              Manage user roles and permissions in the system.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Plus class="h-4 w-4" />
            Add Role
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Roles Overview</CardTitle>
            <CardDescription>
              View, edit or remove roles and assign them to users.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex items-center justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search roles..."
                class="max-w-xs"
              />
            </div>

            <!-- Roles Table -->
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-[200px]">Role</TableHead>
                  <TableHead>Description</TableHead>
                  <TableHead class="w-[100px] text-center">Users</TableHead>
                  <TableHead class="w-20 text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="role in roles"
                  :key="role.id"
                  class="hover:bg-muted/50"
                >
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div
                        class="h-3 w-3 rounded-full"
                        :class="role.color"
                      ></div>
                      <span class="font-medium">{{ role.name }}</span>
                    </div>
                  </TableCell>

                  <TableCell class="text-muted-foreground">
                    {{ role.description }}
                  </TableCell>

                  <TableCell class="text-center">
                    <Badge variant="secondary">
                      <Users class="h-3 w-3 mr-1" />
                      {{ role.users }}
                    </Badge>
                  </TableCell>

                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>Edit Role</DropdownMenuItem>
                        <DropdownMenuItem>Assign Users</DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem class="text-red-600"
                          >Delete Role</DropdownMenuItem
                        >
                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
